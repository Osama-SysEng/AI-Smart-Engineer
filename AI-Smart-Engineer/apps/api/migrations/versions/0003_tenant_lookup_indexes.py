"""Add missing tenant/user lookup indexes for list endpoints.

Revision ID: 0003
Revises: 0002
"""
from alembic import op
import sqlalchemy as sa


revision = "0003"
down_revision = "0002"
branch_labels = None
depends_on = None

WANTED = [
    ("ix_users_tenant_id", "users", ["tenant_id"]),
    ("ix_projects_tenant_id", "projects", ["tenant_id"]),
    ("ix_documents_project_id", "documents", ["project_id"]),
    ("ix_notifications_user_id", "notifications", ["user_id"]),
]


def upgrade() -> None:
    bind = op.get_bind()
    inspector = sa.inspect(bind)
    for name, table, columns in WANTED:
        try:
            existing = {i["name"] for i in inspector.get_indexes(table)}
        except Exception:
            existing = set()
        if name not in existing:
            op.create_index(name, table, columns)


def downgrade() -> None:
    for name, table, _columns in reversed(WANTED):
        try:
            op.drop_index(name, table_name=table)
        except Exception:
            pass
