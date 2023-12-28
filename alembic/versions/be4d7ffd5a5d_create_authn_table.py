"""create authentications table

Revision ID: be4d7ffd5a5d
Revises: 1542a23f27de
Create Date: 2023-12-26 13:13:59.627727

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'be4d7ffd5a5d'
down_revision: Union[str, None] = '1542a23f27de'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'authentications',
        sa.Column('token', sa.String(255), primary_key=True),
    )


def downgrade() -> None:
    op.drop_table('authentications')
