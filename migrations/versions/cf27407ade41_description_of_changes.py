"""Description of changes

Revision ID: cf27407ade41
Revises: f3d76b88340a
Create Date: 2024-03-05 14:35:23.561732

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cf27407ade41'
down_revision = 'f3d76b88340a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('CallBook', schema=None) as batch_op:
        batch_op.add_column(sa.Column('scrip_Code', sa.Integer(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('CallBook', schema=None) as batch_op:
        batch_op.drop_column('scrip_Code')

    # ### end Alembic commands ###
