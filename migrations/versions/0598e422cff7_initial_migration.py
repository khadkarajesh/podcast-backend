"""Initial migration

Revision ID: 0598e422cff7
Revises: 
Create Date: 2020-03-08 10:49:50.783794

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '0598e422cff7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
                    sa.Column('id', sa.VARCHAR(), autoincrement=False, nullable=False),
                    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
                    sa.Column('created_by', sa.VARCHAR(), autoincrement=False, nullable=True),
                    sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
                    sa.Column('updated_by', sa.VARCHAR(), autoincrement=False, nullable=True),
                    sa.Column('username', sa.VARCHAR(), autoincrement=False, nullable=False),
                    sa.Column('password', sa.VARCHAR(), autoincrement=False, nullable=False),
                    sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=False),
                    sa.Column('email_verified', sa.BOOLEAN(), autoincrement=False, nullable=True),
                    sa.PrimaryKeyConstraint('id', name='base_model_pkey')
                    )
    # ### end Alembic commands ###
