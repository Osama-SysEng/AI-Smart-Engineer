# SCALING — AI Smart Engineer API

- Bottleneck: unbounded list endpoints + per-process rate limiting + DB pool exhaustion under concurrent AI/document workloads.
- Tuning: Dockerfile `--workers 4`; pool via settings (`DATABASE_POOL_SIZE=20`, `DATABASE_MAX_OVERFLOW=10`, `pool_pre_ping=True`, `DATABASE_POOL_RECYCLE_SECONDS=1800`); `RATE_LIMIT_PER_MINUTE` (default 600, sliding window per IP+path, `/api/v1/health*` and docs exempt); list endpoints capped `limit=50` default, `500` max (workflows, tasks, runs, recon items, entities, sites, AI usage, notifications).
- Known limits: rate limiter is in-memory per worker (not shared across the 4 workers — use Redis for strict global limits); migration `0003` adds `users/projects.tenant_id`, `documents.project_id`, `notifications.user_id` indexes — verify with `EXPLAIN ANALYZE` on large tenants; heavy AI/document work should stay on Celery workers (`Dockerfile.worker`), not the API pool.
