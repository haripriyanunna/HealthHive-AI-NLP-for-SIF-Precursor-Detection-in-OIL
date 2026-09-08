from datetime import datetime
from sqlalchemy import String, Text, Integer, DateTime, Boolean, JSON, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .database import Base

class Report(Base):
    __tablename__ = "reports"
    id: Mapped[int] = mapped_column(primary_key=True)
    reference: Mapped[str] = mapped_column(String(20), unique=True, index=True)
    reporter_name: Mapped[str] = mapped_column(String(100))
    reporter_id: Mapped[int | None] = mapped_column(ForeignKey("users.id"), nullable=True, index=True)
    site: Mapped[str] = mapped_column(String(160), index=True)
    report_type: Mapped[str] = mapped_column(String(40))
    language: Mapped[str] = mapped_column(String(12), default="en-IN")
    narrative: Mapped[str] = mapped_column(Text)
    risk_level: Mapped[str] = mapped_column(String(12), index=True)
    risk_score: Mapped[int] = mapped_column(Integer)
    iogp_rule: Mapped[str | None] = mapped_column(String(80), nullable=True)
    confidence: Mapped[int] = mapped_column(Integer)
    precursor_signals: Mapped[list[str]] = mapped_column(JSON, default=list)
    rationale: Mapped[str] = mapped_column(Text, default="")
    needs_human_review: Mapped[bool] = mapped_column(Boolean, default=True)
    status: Mapped[str] = mapped_column(String(30), default="Needs review")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    reporter: Mapped["User | None"] = relationship(back_populates="reports")

class User(Base):
    """Master identity record. Store a password hash from an approved auth provider in production."""
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    full_name: Mapped[str] = mapped_column(String(100))
    employee_id: Mapped[str] = mapped_column(String(60), unique=True, index=True)
    role: Mapped[str] = mapped_column(String(20), index=True)  # worker or supervisor
    site: Mapped[str | None] = mapped_column(String(160), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    reports: Mapped[list["Report"]] = relationship(back_populates="reporter")

class Site(Base):
    """Master site list, managed by a supervisor or organization administrator."""
    __tablename__ = "sites"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(160), unique=True)
    region: Mapped[str | None] = mapped_column(String(100), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
