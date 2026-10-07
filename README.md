# AI Smart Engineer

Engineering Intelligence and Automation Platform.
FastAPI backend plus Next.js frontend in one monorepo.

## Where is the real project?

All source code lives in `AI-Smart-Engineer/`:

- `AI-Smart-Engineer/apps/api/` - FastAPI backend (Python 3.11)
- `AI-Smart-Engineer/apps/web/` - Next.js frontend (React + TypeScript)
- `AI-Smart-Engineer/ARCHITECTURE.md` - system architecture
- `AI-Smart-Engineer/docker-compose.yml` - full stack orchestration
- `AI-Smart-Engineer/README.md` - full documentation

## Quick start

```bash
cd AI-Smart-Engineer
cp .env.example .env
docker-compose up -d
docker-compose exec api alembic upgrade head
```

- Web: http://localhost:3000
- API docs: http://localhost:8000/docs

## Tests

```bash
cd AI-Smart-Engineer/apps/api
python -m pytest -q
```
