# PRD — AI-Smart-Engineer (المهندس الذكي)
## 1. نظرة عامة
- منصة هندسة ذكية: مستندات، استخراج AI بثقة، مطابقة-mصادر، شذوذ، SAP، Workflows.
- Backend: FastAPI (`apps/api/src/main.py`) ببادئة `/api/v1/...`.
- Web: Next.js على `:3000`. API Docs: `:8000/docs`. مهام: Celery.
## 2. المستخدمون
1. مهندس — مشاريع ومستندات واستخراج.
2. مراجع/معتمد — مطابقة وعناصر وworkflows (human-in-the-loop).
3. مدير/مدقق — تقارير وتدقيق وصلاحيات RBAC.
4. مشغّل AI — محادثة ومراقبة استخدام وتكلفة.
## 3. الميزات الأساسية (قابلة للاختبار)
1. تسجيل مستخدم جديد عبر `/auth/register`.
2. تسجيل دخول JWT عبر `/auth/login` + refresh + logout + بياناتي `/auth/me`.
3. إنشاء/عرض مشروع + مواقع + أقسام.
4. رفع مستند + عرضه + عرض كياناته المستخرجة.
5. تشغيل استخراج (202) + تتبع runs.
6. تشغيل مطابقة (202) + عرض عناصر run + اعتماد عنصر.
7. إنشاء/عرض workflows + runs + مهام.
8. محادثة AI نصية + WebSocket + عرض الاستخدام والمزودين.
9. توليد تقارير + عرض أنواعها.
10. تحليلات dashboard/KPIs + إشعارات (قراءة/تعميم الكل).
11. سجل تدقيق (logs/events) + صلاحيات (effective/roles).
12. فحوصات health/ready/live/dependencies.
## 4. الـAPI endpoints الحقيقية (من الكود فقط)
- `POST /api/v1/auth/register` / `POST /api/v1/auth/login`
- `GET /api/v1/auth/me` / `POST /api/v1/auth/refresh` / `POST /api/v1/auth/logout`
- `POST /api/v1/projects` / `GET /api/v1/projects` / `GET /api/v1/projects/{project_id}`
- `POST /api/v1/projects/{project_id}/sites` / `GET .../sites`
- `POST /api/v1/projects/{project_id}/departments`
- `POST /api/v1/documents/upload` / `GET /api/v1/documents`
- `GET /api/v1/documents/{document_id}` / `GET .../entities`
- `POST /api/v1/extraction/run` / `GET /api/v1/extraction/runs` / `GET /api/v1/extraction/runs/{run_id}`
- `POST /api/v1/reconciliation/run` / `GET /api/v1/reconciliation/runs/{run_id}`
- `GET /api/v1/reconciliation/runs/{run_id}/items` / `POST /api/v1/reconciliation/items/{item_id}/approve`
- `POST /api/v1/workflows` / `GET /api/v1/workflows` / `GET /api/v1/workflows/{workflow_id}/runs`
- `POST /api/v1/workflows/tasks` / `GET /api/v1/workflows/tasks`
- `POST /api/v1/ai/chat` / `WS /api/v1/ai/ws/chat` / `GET /api/v1/ai/usage` / `GET /api/v1/ai/providers`
- `POST /api/v1/reports/generate` / `GET /api/v1/reports/types`
- `GET /api/v1/analytics/dashboard` / `GET /api/v1/analytics/kpis`
- `GET /api/v1/notifications` / `POST .../{notification_id}/read` / `POST .../mark-all-read`
- `GET /api/v1/audit/logs|events` / `GET /api/v1/security/effective` / `POST .../permissions|roles`
- `GET /api/v1/health|ready|live|dependencies` / `GET /`
## 5. بيانات الدخول/الإعداد للاختبار
- انسخ `.env.example` إلى `.env` (يتطلب `SECRET_KEY` 32+ حرفًا).
- عيّن `DATABASE_URL` + `REDIS_URL` محليًا.
- التشغيل: `docker-compose up -d` ثم `alembic upgrade head`.
- العتبات: `CONFIDENCE_AUTO_ACCEPT=0.95` و`CONFIDENCE_REVIEW=0.80`.
- الاختبارات: `pytest apps/api/tests/ -v`.
## 6. خارج النطاق (mocked/simulated — صراحة)
- SAP افتراضيًا read-only/dry-run (`SAP_READ_ONLY/SAP_DRY_RUN=true`) — لا كتابة حقيقية.
- مزودو AI (`OPENAI/ANTHROPIC/GOOGLE/DEEPSEEK/LOCAL`) يحتاجون مفاتيح.
- بدون مفاتيح تُختبر المسارات والأخطاء وضبط التكلفة (`AI_COST_LIMIT_*`) فقط.
- التخزين `local` افتراضيًا؛ S3/Minio وQdrant اختيارية غير مطلوبة للاختبار.
