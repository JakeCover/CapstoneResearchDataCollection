"""Created the rune lookup table

Revision ID: 7d9515d301c7
Revises: 913a7c94a17a
Create Date: 2020-02-11 11:21:28.914158

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7d9515d301c7'
down_revision = '913a7c94a17a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('runes_lookup',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=25), nullable=False),
    sa.Column('shortDesc', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('runes_lookup')
    # ### end Alembic commands ###
