"""merge heads

Revision ID: 8a08f92f8688
Revises: ac64aef8dc5b, e3de16b3eddf
Create Date: 2025-05-28 19:50:25.090686
"""

from alembic import op
import sqlalchemy as sa
from typing import Sequence, Union

# revision identifiers, used by Alembic.
revision: str = '8a08f92f8688'
down_revision: Union[str, Sequence[str]] = ('ac64aef8dc5b', 'e3de16b3eddf')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    pass

def downgrade() -> None:
    pass
