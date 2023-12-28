"""create threads table

Revision ID: b76235e8d9d0
Revises: be4d7ffd5a5d
Create Date: 2023-12-27 10:10:34.657995

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import ForeignKey

# revision identifiers, used by Alembic.
revision: str = 'b76235e8d9d0'
down_revision: Union[str, None] = 'be4d7ffd5a5d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'threads',
        sa.Column('id', sa.String(32), primary_key=True),
        sa.Column('title', sa.String(255), nullable=False),
        sa.Column('owner', sa.String(32), ForeignKey("users.id"), nullable=False),
        sa.Column('body', sa.String(32), nullable=False),
        sa.Column('date', sa.String(32), nullable=False),
    )


def downgrade() -> None:
    op.drop_table('threads')
