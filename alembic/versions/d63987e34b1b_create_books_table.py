"""create books table

Revision ID: d63987e34b1b
Revises:
Create Date: 2023-01-26 09:18:08.277061

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "d63987e34b1b"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "books",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("title", sa.String(255), unique=True, nullable=False),
        sa.Column("author", sa.String(255), nullable=False),
        sa.Column("content", sa.Text, nullable=False),
        sa.Column("pages", sa.Integer, nullable=False),
        sa.Column("created_at", sa.TIMESTAMP, nullable=False),
        sa.Column("last_updated", sa.TIMESTAMP, nullable=False),
    )


def downgrade() -> None:
    op.drop_table("books")
