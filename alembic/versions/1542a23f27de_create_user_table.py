"""create user table

Revision ID: 1542a23f27de
Revises: 
Create Date: 2023-12-25 18:27:37.874537

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1542a23f27de'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.String(length=36), nullable=False, primary_key=True),
        sa.Column("username", sa.String(length=255), nullable=False),
        sa.Column("password", sa.String(length=255), nullable=False),
        sa.Column("fullname", sa.String(length=255), nullable=False),
    )


def downgrade() -> None:
    op.drop_table("users")
