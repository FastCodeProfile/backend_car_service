"""empty message

Revision ID: dac8eb9adbca
Revises: 3bbc2e9381ab
Create Date: 2023-10-03 18:23:57.504943

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dac8eb9adbca'
down_revision = '3bbc2e9381ab'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vinnumber',
    sa.Column('user_fk', sa.Integer(), nullable=False),
    sa.Column('number', sa.String(), nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.ForeignKeyConstraint(['user_fk'], ['user.id'], name=op.f('fk_vinnumber_user_fk_user'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_vinnumber'))
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vinnumber')
    # ### end Alembic commands ###
