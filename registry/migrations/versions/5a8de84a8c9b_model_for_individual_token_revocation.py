"""Model for individual token revocation

Revision ID: 5a8de84a8c9b
Revises: 15f3b51db974
Create Date: 2018-04-19 14:07:59.169169

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '5a8de84a8c9b'
down_revision = '15f3b51db974'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('token',
    sa.Column('user_id', postgresql.UUID(), nullable=False),
    sa.Column('token', postgresql.UUID(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'token')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('token')
    # ### end Alembic commands ###