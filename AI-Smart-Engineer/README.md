# AI Smart Engineer - المهندس الذكي

## Engineering Intelligence & Automation Platform

A comprehensive AI-powered engineering platform for document processing, data extraction, validation, reconciliation, and ERP integration.

## Architecture

```
                    AI SMART ENGINEER
                           │
                    Web Application (Next.js)
                           │
                    API Gateway (FastAPI)
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
   Auth Service      Project Service    Document Service
        │                  │                  │
        └──────────────────┼──────────────────┘
                           │
                    Workflow Engine
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
 AI Engine          Data Engine        Automation Engine
        │                  │                  │
        └──────────────────┼──────────────────┘
                           │
                 Reconciliation Engine
                           │
                 Decision Engine
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
      SAP              PostgreSQL         Object Storage
        │                  │                  │
        └──────────────────┼──────────────────┘
                           │
                  Monitoring / Audit
```

## Quick Start

```bash
# Clone and setup
git clone <repo>
cd ai-smart-engineer

# Environment
cp .env.example .env

# Start all services
docker-compose up -d

# Run migrations
docker-compose exec api alembic upgrade head

# Access
# Web App: http://localhost:3000
# API Docs: http://localhost:8000/docs
# Adminer: http://localhost:8080
# Redis Commander: http://localhost:8081
```

## Project Structure

- `apps/web/src/` - Next.js frontend (React, TypeScript, Tailwind)
- `apps/api/src/` - FastAPI backend (Python, async, modular: `auth/`, `projects/`, `documents/`, `extraction/`, `reconciliation/`, `workflows/`, `ai/`, `agents/`, `integrations/sap/`, `services/`, `queue/` Celery workers, `security/`, `audit/`)
- `apps/api/tests/` - backend test suite (pytest)
- `apps/api/migrations/` - Alembic migrations (baseline `0001`, `0002` head)
- `infrastructure/` - Docker, K8s, Terraform
- `docs/` - documentation
- `tools/` - operational tooling
- `reports/` - generated reports

## Features

- Document Intelligence (OCR, Layout Detection, Table Extraction)
- Excel Intelligence (Formula Analysis, Validation)
- AI Extraction with Confidence Scoring
- Cross-Source Reconciliation
- Anomaly Detection (Rule + Statistical + AI)
- SAP Integration with Audit Trail
- Workflow Automation Engine
- Human-in-the-Loop Approval
- Real-time Notifications
- Advanced Search (Keyword + Semantic)
- Knowledge Graph
- Multi-tenant Ready
- RBAC Security
- Full Audit Trail
- AI Cost Control & Routing

## License

Proprietary - AI Smart Engineer Platform


## Hardening status

This build includes tenant-aware project/document access checks, explicit CORS configuration, production secret validation, upload size enforcement, authenticated AI WebSocket sessions, Docker build fixes, and CI checks. SAP remains read-only/dry-run by default.
