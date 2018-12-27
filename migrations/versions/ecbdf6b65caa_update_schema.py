"""update schema

Revision ID: ecbdf6b65caa
Revises: de18ff7213c1
Create Date: 2018-12-27 15:05:37.155953

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ecbdf6b65caa'
down_revision = 'de18ff7213c1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('submissions', sa.Column('submitted_by', sa.Integer(), nullable=True))
    op.drop_constraint('submissions_account_id_fkey', 'submissions', type_='foreignkey')
    op.create_foreign_key(None, 'submissions', 'accounts', ['submitted_by'], ['id'])
    op.drop_column('submissions', 'account_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('submissions', sa.Column('account_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'submissions', type_='foreignkey')
    op.create_foreign_key('submissions_account_id_fkey', 'submissions', 'accounts', ['account_id'], ['id'])
    op.drop_column('submissions', 'submitted_by')
    # ### end Alembic commands ###