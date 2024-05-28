"""update users table

Revision ID: ed30a8f17cf4
Revises: 4810a9cdb58d
Create Date: 2024-05-09 22:06:03.195166

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "ed30a8f17cf4"
down_revision: Union[str, None] = "4810a9cdb58d"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("users", sa.Column("foo", sa.Integer(), nullable=False))
    op.add_column("users", sa.Column("bar", sa.Integer(), nullable=False))
    op.create_unique_constraint(
        op.f("uq_users_foo_bar"), "users", ["foo", "bar"]
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f("uq_users_foo_bar"), "users", type_="unique")
    op.drop_column("users", "bar")
    op.drop_column("users", "foo")
    # ### end Alembic commands ###