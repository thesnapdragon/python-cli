"""add_initial_schema

Revision ID: 0fbc5f505c79
Revises: 
Create Date: 2016-06-26 18:50:23.985724

"""

# revision identifiers, used by Alembic.
revision = '0fbc5f505c79'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'examples',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
    )


def downgrade():
    op.drop_table('examples')
