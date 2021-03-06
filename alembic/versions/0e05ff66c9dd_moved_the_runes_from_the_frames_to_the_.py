"""Moved the runes from the frames to the metadata

Revision ID: 0e05ff66c9dd
Revises: 91e2634409cd
Create Date: 2020-03-04 10:59:35.701732

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '0e05ff66c9dd'
down_revision = '91e2634409cd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('game_frames', 'second_rune')
    op.drop_column('game_frames', 'main_rune')
    op.drop_column('game_frames', 'rune_choices')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('game_frames', sa.Column('rune_choices', postgresql.ARRAY(sa.INTEGER()), autoincrement=False, nullable=False))
    op.add_column('game_frames', sa.Column('main_rune', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('game_frames', sa.Column('second_rune', sa.INTEGER(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
