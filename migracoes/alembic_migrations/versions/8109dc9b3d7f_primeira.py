"""primeira

Revision ID: 8109dc9b3d7f
Revises: 
Create Date: 2024-06-25 07:23:39.023787

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8109dc9b3d7f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'pessoa',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('nome', sa.String(length=50), nullable=False),
        sa.Column('email', sa.String(length=50), nullable=False)
    )


def downgrade() -> None:
    op.drop_table('pessoa')
