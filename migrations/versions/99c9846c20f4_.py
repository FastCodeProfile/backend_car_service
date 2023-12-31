"""empty message

Revision ID: 99c9846c20f4
Revises: dac8eb9adbca
Create Date: 2023-10-03 19:18:33.578381

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '99c9846c20f4'
down_revision = 'dac8eb9adbca'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('carservice',
    sa.Column('user_fk', sa.Integer(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('service', sa.Text(), nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.ForeignKeyConstraint(['user_fk'], ['user.id'], name=op.f('fk_carservice_user_fk_user'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_carservice'))
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('carservice')
    # ### end Alembic commands ###
