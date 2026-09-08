-- HealthHive PostgreSQL database schema
-- Run this in Supabase SQL Editor, pgAdmin, or psql before starting the API.

CREATE TABLE IF NOT EXISTS users (
    id BIGSERIAL PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    employee_id VARCHAR(60) NOT NULL UNIQUE,
    role VARCHAR(20) NOT NULL CHECK (role IN ('worker', 'supervisor')),
    site VARCHAR(160),
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS ix_users_role ON users(role);

CREATE TABLE IF NOT EXISTS sites (
    id BIGSERIAL PRIMARY KEY,
    name VARCHAR(160) NOT NULL UNIQUE,
    region VARCHAR(100),
    is_active BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE IF NOT EXISTS reports (
    id BIGSERIAL PRIMARY KEY,
    reference VARCHAR(20) NOT NULL UNIQUE,
    reporter_name VARCHAR(100) NOT NULL,
    reporter_id BIGINT REFERENCES users(id),
    site VARCHAR(160) NOT NULL,
    report_type VARCHAR(40) NOT NULL,
    language VARCHAR(12) NOT NULL DEFAULT 'en-IN',
    narrative TEXT NOT NULL,
    risk_level VARCHAR(12) NOT NULL,
    risk_score INTEGER NOT NULL CHECK (risk_score BETWEEN 0 AND 100),
    iogp_rule VARCHAR(80),
    confidence INTEGER NOT NULL CHECK (confidence BETWEEN 0 AND 100),
    precursor_signals JSONB NOT NULL DEFAULT '[]'::jsonb,
    rationale TEXT NOT NULL DEFAULT '',
    needs_human_review BOOLEAN NOT NULL DEFAULT TRUE,
    status VARCHAR(30) NOT NULL DEFAULT 'Needs review',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS ix_reports_reporter_id ON reports(reporter_id);
CREATE INDEX IF NOT EXISTS ix_reports_site ON reports(site);
CREATE INDEX IF NOT EXISTS ix_reports_risk_level ON reports(risk_level);

-- Optional seed records for the prototype
INSERT INTO sites (name, region) VALUES
    ('Duliajan Drill Pad 4', 'Assam'),
    ('Moran Tank Farm', 'Assam'),
    ('Naharkatiya Well 12', 'Assam')
ON CONFLICT (name) DO NOTHING;
