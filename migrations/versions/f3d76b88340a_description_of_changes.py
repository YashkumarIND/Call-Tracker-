"""Description of changes

Revision ID: f3d76b88340a
Revises: cb9431271ddc
Create Date: 2024-03-05 13:47:04.278766

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f3d76b88340a'
down_revision = 'cb9431271ddc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('scrip_code',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('scrip_code', sa.Integer(), nullable=False),
    sa.Column('tick_size', sa.Float(), nullable=False),
    sa.Column('inst_type', sa.String(length=50), nullable=False),
    sa.Column('company_name', sa.String(length=255), nullable=False),
    sa.Column('indices', sa.String(length=255), nullable=False),
    sa.Column('industry', sa.String(length=255), nullable=False),
    sa.Column('isin_code', sa.String(length=50), nullable=False),
    sa.Column('trading_symbol', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('scrip_code')
    # ### end Alembic commands ###
