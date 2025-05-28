"""merge initial and additional migrations

Revision ID: f7037bfe20b0
Revises: ac64aef8dc5b, e3de16b3eddf
Create Date: 2025-05-28 19:35:10.773765
"""

from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa


revision: str = 'f7037bfe20b0'
down_revision: Union[str, tuple[str, ...]] = ('ac64aef8dc5b', 'e3de16b3eddf')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    pass

def downgrade() -> None:
    pass
