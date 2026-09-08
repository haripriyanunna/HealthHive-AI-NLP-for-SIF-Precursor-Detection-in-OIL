from datetime import datetime
from pydantic import BaseModel, Field

class ReportCreate(BaseModel):
    reporter_name: str = Field(min_length=2, max_length=100)
    reporter_id: int | None = None
    site: str = Field(min_length=2, max_length=160)
    report_type: str
    language: str = "en-IN"
    narrative: str = Field(min_length=10, max_length=5000)

class Classification(BaseModel):
    risk_level: str
    risk_score: int
    iogp_rule: str | None
    precursor_signals: list[str]
    confidence: int
    needs_human_review: bool
    rationale: str

class ReportOut(ReportCreate, Classification):
    reference: str
    status: str
    created_at: datetime
    class Config: from_attributes = True

class StatusUpdate(BaseModel): status: str

class UserRegister(BaseModel):
    full_name: str = Field(min_length=2, max_length=100)
    employee_id: str = Field(min_length=2, max_length=60)
    role: str
    site: str | None = Field(default=None, max_length=160)

class UserOut(UserRegister):
    id: int
    is_active: bool
    created_at: datetime
    class Config: from_attributes = True

class SiteCreate(BaseModel):
    name: str = Field(min_length=2, max_length=160)
    region: str | None = Field(default=None, max_length=100)

class SiteOut(SiteCreate):
    id: int
    is_active: bool
    class Config: from_attributes = True
