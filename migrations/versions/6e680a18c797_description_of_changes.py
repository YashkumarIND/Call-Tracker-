"""Description of changes

Revision ID: 6e680a18c797
Revises: cf27407ade41
Create Date: 2024-03-05 15:19:56.798570

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6e680a18c797'
down_revision = 'cf27407ade41'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('scrip_code', schema=None) as batch_op:
        batch_op.alter_column('indices',
               existing_type=sa.VARCHAR(length=255),
               type_=sa.TEXT(),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('scrip_code', schema=None) as batch_op:
        batch_op.alter_column('indices',
               existing_type=sa.TEXT(),
               type_=sa.VARCHAR(length=255),
               existing_nullable=False)

    # ### end Alembic commands ###