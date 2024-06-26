"""Add Status column to CallBook table

Revision ID: 2f32d632b209
Revises: 2029919c017c
Create Date: 2024-02-19 13:13:37.279044

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2f32d632b209'
down_revision = '2029919c017c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('trade')
    with op.batch_alter_table('call_book', schema=None) as batch_op:
        batch_op.add_column(sa.Column('Status', sa.String(length=50), nullable=False))
        batch_op.drop_column('Success')
        batch_op.drop_column('GainLoss')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('call_book', schema=None) as batch_op:
        batch_op.add_column(sa.Column('GainLoss', sa.FLOAT(), nullable=True))
        batch_op.add_column(sa.Column('Success', sa.BOOLEAN(), nullable=True))
        batch_op.drop_column('Status')

    op.create_table('trade',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('tradingSymbol', sa.VARCHAR(length=50), nullable=False),
    sa.Column('BuyPrice', sa.FLOAT(), nullable=False),
    sa.Column('Target', sa.FLOAT(), nullable=False),
    sa.Column('StopLoss', sa.FLOAT(), nullable=False),
    sa.Column('Success', sa.BOOLEAN(), nullable=True),
    sa.Column('GainLoss', sa.FLOAT(), nullable=True),
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
