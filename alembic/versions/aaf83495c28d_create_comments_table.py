"""create comments table

Revision ID: aaf83495c28d
Revises: b76235e8d9d0
Create Date: 2023-12-28 07:05:18.023985

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'aaf83495c28d'
down_revision: Union[str, None] = 'b76235e8d9d0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'comments',
        sa.Column('id', sa.String(32), primary_key=True),
        sa.Column('content', sa.String(32), nullable=False),
        sa.Column('owner', sa.String(32), sa.ForeignKey("users.id"), nullable=False),
        sa.Column('thread_id', sa.String(32), sa.ForeignKey("threads.id"), nullable=False),
        sa.Column('is_deleted', sa.Boolean, nullable=False, default=False),
        sa.Column('date', sa.String(32), nullable=False),
    )


def downgrade() -> None:
    op.drop_table('comments')
