"""init_collectors

Revision ID: 4b88da371ba9
Revises: 5eaff17eaece
Create Date: 2023-11-30 13:39:25.538560

"""
import sqlalchemy as sa  # noqa: F401
import sqlmodel  # noqa: F401
from alembic import op

# revision identifiers, used by Alembic.
revision = "4b88da371ba9"
down_revision = "5eaff17eaece"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "collector",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("address", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("zip_code", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("city", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("lat", sa.Float(), nullable=False),
        sa.Column("lng", sa.Float(), nullable=False),
        sa.Column("email", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("phone", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column(
            "created_at", sa.TIMESTAMP(timezone=True), server_default=sa.text("CURRENT_TIMESTAMP"), nullable=False
        ),
        sa.Column(
            "updated_at", sa.TIMESTAMP(timezone=True), server_default=sa.text("CURRENT_TIMESTAMP"), nullable=False
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    collector_collection_type_table = op.create_table(
        "collector_collection_type",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_collector_collection_type_name"), "collector_collection_type", ["name"], unique=True)
    op.bulk_insert(
        collector_collection_type_table,
        [
            {"id": 1, "name": "Inert Waste"},
            {"id": 2, "name": "Concrete"},
            {"id": 3, "name": "Wood"},
            {"id": 4, "name": "Metals"},
            {"id": 5, "name": "Plaster"},
            {"id": 6, "name": "Rigid Plastics & PVC"},
            {"id": 7, "name": "Glazed Joinery"},
            {"id": 8, "name": "Glass Wool"},
            {"id": 9, "name": "Rock Wool"},
            {"id": 10, "name": "Expanded Polystyrene (EPS)"},
            {"id": 11, "name": "Polyurethane"},
            {"id": 12, "name": "Bio-based Insulators"},
            {"id": 13, "name": "Bituminous Membranes"},
            {"id": 14, "name": "Non-PVC Floor Coverings"},
            {"id": 15, "name": "PVC Floor Coverings"},
        ],
    )
    op.create_table(
        "collector_to_collector_collection_type",
        sa.Column("collector_id", sa.Integer(), nullable=False),
        sa.Column("collector_collection_type_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["collector_collection_type_id"],
            ["collector_collection_type.id"],
        ),
        sa.ForeignKeyConstraint(
            ["collector_id"],
            ["collector.id"],
        ),
        sa.PrimaryKeyConstraint("collector_id", "collector_collection_type_id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("collector_to_collector_collection_type")
    op.drop_index(op.f("ix_collector_collection_type_name"), table_name="collector_collection_type")
    op.drop_table("collector_collection_type")
    op.drop_table("collector")
    # ### end Alembic commands ###
