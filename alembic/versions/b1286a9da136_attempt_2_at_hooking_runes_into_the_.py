"""Attempt 2 at hooking runes into the rune choices row, split up the runes array

Revision ID: b1286a9da136
Revises: 942a338729c5
Create Date: 2020-02-12 10:30:38.009061

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b1286a9da136'
down_revision = '942a338729c5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('game_frames', sa.Column('rune_choices_1', sa.Integer(), nullable=True))
    op.add_column('game_frames', sa.Column('rune_choices_2', sa.Integer(), nullable=True))
    op.add_column('game_frames', sa.Column('rune_choices_3', sa.Integer(), nullable=True))
    op.add_column('game_frames', sa.Column('rune_choices_4', sa.Integer(), nullable=True))
    op.add_column('game_frames', sa.Column('rune_choices_5', sa.Integer(), nullable=True))
    op.add_column('game_frames', sa.Column('rune_choices_6', sa.Integer(), nullable=True))
    op.add_column('game_frames', sa.Column('rune_choices_7', sa.Integer(), nullable=True))
    op.add_column('game_frames', sa.Column('rune_choices_8', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'game_frames', 'runes_lookup', ['rune_choices_6'], ['id'])
    op.create_foreign_key(None, 'game_frames', 'runes_lookup', ['rune_choices_2'], ['id'])
    op.create_foreign_key(None, 'game_frames', 'runes_lookup', ['rune_choices_1'], ['id'])
    op.create_foreign_key(None, 'game_frames', 'runes_lookup', ['rune_choices_7'], ['id'])
    op.create_foreign_key(None, 'game_frames', 'runes_lookup', ['rune_choices_5'], ['id'])
    op.create_foreign_key(None, 'game_frames', 'runes_lookup', ['rune_choices_4'], ['id'])
    op.create_foreign_key(None, 'game_frames', 'runes_lookup', ['rune_choices_8'], ['id'])
    op.create_foreign_key(None, 'game_frames', 'runes_lookup', ['rune_choices_3'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'game_frames', type_='foreignkey')
    op.drop_constraint(None, 'game_frames', type_='foreignkey')
    op.drop_constraint(None, 'game_frames', type_='foreignkey')
    op.drop_constraint(None, 'game_frames', type_='foreignkey')
    op.drop_constraint(None, 'game_frames', type_='foreignkey')
    op.drop_constraint(None, 'game_frames', type_='foreignkey')
    op.drop_constraint(None, 'game_frames', type_='foreignkey')
    op.drop_column('game_frames', 'rune_choices_8')
    op.drop_column('game_frames', 'rune_choices_7')
    op.drop_column('game_frames', 'rune_choices_6')
    op.drop_column('game_frames', 'rune_choices_5')
    op.drop_column('game_frames', 'rune_choices_4')
    op.drop_column('game_frames', 'rune_choices_3')
    op.drop_column('game_frames', 'rune_choices_2')
    op.drop_column('game_frames', 'rune_choices_1')
    # ### end Alembic commands ###
