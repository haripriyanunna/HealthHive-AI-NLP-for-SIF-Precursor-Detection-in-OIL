"""HealthHive prototype API. The classifier supports triage, never a final safety decision."""
from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from .database import Base, engine, get_db, settings
from .models import Report, User, Site
from .schemas import ReportCreate, ReportOut, Classification, StatusUpdate, UserRegister, UserOut, SiteCreate, SiteOut

SIGNALS = {
    "fire / explosion": ["leak", "gas", "flammable", "fire", "hot", "spark", "pressure"],
    "line of fire": ["lifting", "load", "rotary", "struck", "pinch", "line of fire"],
    "energy isolation": ["isolation", "lockout", "energized", "electrical", "hydraulic"],
    "working at height": ["height", "fall", "scaffold", "ladder", "handrail"],
    "vehicle safety": ["vehicle", "truck", "reversing", "traffic"]
}
def classify_report(text: str) -> Classification:
    """Explainable prompt-style fallback; replace with an approved LLM prompt service in production."""
    lower = text.lower(); hits = [(rule, word) for rule, words in SIGNALS.items() for word in words if word in lower]
    rules = list(dict.fromkeys(rule for rule, _ in hits)); words = list(dict.fromkeys(word for _, word in hits))
    score = min(96, 38 + len(words) * 13 + (15 if len(rules) > 1 else 0))
    level = "High" if score >= 75 else "Medium" if score >= 55 else "Low"
    confidence = min(92, 55 + len(words) * 8)
    review = confidence < 78 or level == "High"
    return Classification(risk_level=level, risk_score=score, iogp_rule=rules[0] if rules else None,
      precursor_signals=words or ["No strong lexical signal detected"], confidence=confidence,
      needs_human_review=review, rationale="Possible high-energy exposure requires supervisor validation." if hits else "Insufficient signal; supervisor review protects against missed risk.")

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine); yield
app = FastAPI(title="HealthHive Safety API", version="0.1.0", lifespan=lifespan)
app.add_middleware(CORSMiddleware, allow_origins=[x.strip() for x in settings.allowed_origins.split(',')], allow_methods=["*"], allow_headers=["*"], allow_credentials=True)

@app.get("/health")
def health(): return {"status":"ok"}
@app.post("/users/register", response_model=UserOut, status_code=201)
def register_user(payload: UserRegister, db: Session = Depends(get_db)):
    if payload.role not in {"worker", "supervisor"}:
        raise HTTPException(422, "Role must be worker or supervisor")
    existing = db.query(User).filter(User.employee_id == payload.employee_id).first()
    if existing:
        return existing  # repeat registration safely returns the master record
    user = User(**payload.model_dump())
    db.add(user); db.commit(); db.refresh(user); return user
@app.get("/users", response_model=list[UserOut])
def list_users(db: Session = Depends(get_db)):
    return db.query(User).filter(User.is_active == True).order_by(User.full_name).all()
@app.post("/sites", response_model=SiteOut, status_code=201)
def create_site(payload: SiteCreate, db: Session = Depends(get_db)):
    if db.query(Site).filter(Site.name == payload.name).first(): raise HTTPException(409, "Site already exists")
    site = Site(**payload.model_dump()); db.add(site); db.commit(); db.refresh(site); return site
@app.get("/sites", response_model=list[SiteOut])
def list_sites(db: Session = Depends(get_db)):
    return db.query(Site).filter(Site.is_active == True).order_by(Site.name).all()
@app.post("/classify", response_model=Classification)
def classify(payload: ReportCreate): return classify_report(payload.narrative)
@app.post("/reports", response_model=ReportOut, status_code=201)
def create_report(payload: ReportCreate, db: Session = Depends(get_db)):
    if payload.reporter_id and not db.get(User, payload.reporter_id):
        raise HTTPException(422, "Registered reporter not found")
    result = classify_report(payload.narrative)
    count = db.query(Report).count() + 1001
    report = Report(reference=f"HH-{count}", **payload.model_dump(), **result.model_dump(), status="Needs review")
    db.add(report); db.commit(); db.refresh(report); return report
@app.get("/reports", response_model=list[ReportOut])
def list_reports(db: Session = Depends(get_db)):
    return db.query(Report).order_by(Report.created_at.desc()).all()
@app.patch("/reports/{reference}/status", response_model=ReportOut)
def update_status(reference: str, payload: StatusUpdate, db: Session = Depends(get_db)):
    report = db.query(Report).filter(Report.reference == reference).first()
    if not report: raise HTTPException(404, "Report not found")
    report.status = payload.status; db.commit(); db.refresh(report); return report
