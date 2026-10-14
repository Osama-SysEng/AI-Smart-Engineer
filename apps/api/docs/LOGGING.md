# Structured Logging (AI Smart Engineer API)

Stdlib-only JSON logging via `src/core/logging_utils.py` (no new dependencies).
The existing structlog setup in `src/core/logging.py` is unchanged; request
context is shared through `logging_utils.request_id_ctx`.

## One line per request

`add_request_id` in `src/main.py` echoes/propagates `X-Request-ID` and emits a
single access line:

```json
{"event": "http.access", "method": "GET", "path": "/api/v1/health",
 "status_code": 200, "request_id": "…", "duration_ms": 1.2,
 "level": "info", "timestamp": "..."}
```

## Env (.env.example)

| Var | Purpose | Default |
| --- | ------- | ------- |
| `SERVICE_NAME` | `service` field | `ai-smart-engineer` |
| `LOG_LEVEL` | min level | `INFO` (`debug` outside production) |
| `GIT_SHA` | `version` field | `dev` |
| `ENVIRONMENT` | `env` field | `development` |

## Rules

- Never log secrets — keys containing `password/token/secret/api_key/authorization/cookie/...` are redacted as `***` in `logging_utils` extras.
- No `print()` in runtime code (`src/`); use `get_logger(__name__)`.
- Correlate with `X-Request-ID` (also in error responses as `request_id`).
