"""add projects images detections

Revision ID: a1b2c3d4e5f6
Revises: b23679511c3c
Create Date: 2026-01-30 16:14:15.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a1b2c3d4e5f6'
down_revision: Union[str, Sequence[str], None] = 'b23679511c3c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # Create projects table
    op.create_table('projects',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('owner_id', sa.Integer(), nullable=False),
        sa.Column('is_public', sa.Boolean(), nullable=True, default=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
        sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index('idx_projects_id', 'projects', ['id'], unique=False)
    op.create_index('idx_projects_owner_id', 'projects', ['owner_id'], unique=False)

    # Create images table
    op.create_table('images',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('filename', sa.String(), nullable=False),
        sa.Column('original_filename', sa.String(), nullable=False),
        sa.Column('file_path', sa.String(), nullable=False),
        sa.Column('file_size', sa.Integer(), nullable=True),
        sa.Column('mime_type', sa.String(), nullable=True),
        sa.Column('width', sa.Integer(), nullable=True),
        sa.Column('height', sa.Integer(), nullable=True),
        sa.Column('latitude', sa.Float(), nullable=True),
        sa.Column('longitude', sa.Float(), nullable=True),
        sa.Column('captured_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('uploaded_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.Column('project_id', sa.Integer(), nullable=False),
        sa.Column('uploaded_by_id', sa.Integer(), nullable=False),
        sa.Column('processing_status', sa.String(), nullable=True, default='pending'),
        sa.Column('processing_started_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('processing_completed_at', sa.DateTime(timezone=True), nullable=True),
        sa.ForeignKeyConstraint(['project_id'], ['projects.id'], ),
        sa.ForeignKeyConstraint(['uploaded_by_id'], ['users.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index('idx_images_id', 'images', ['id'], unique=False)
    op.create_index('idx_images_project_id', 'images', ['project_id'], unique=False)
    op.create_index('idx_images_uploaded_by_id', 'images', ['uploaded_by_id'], unique=False)

    # Create detections table
    op.create_table('detections',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('image_id', sa.Integer(), nullable=False),
        sa.Column('species_name', sa.String(), nullable=False),
        sa.Column('confidence_score', sa.Float(), nullable=False),
        sa.Column('bbox_x_min', sa.Float(), nullable=False),
        sa.Column('bbox_y_min', sa.Float(), nullable=False),
        sa.Column('bbox_x_max', sa.Float(), nullable=False),
        sa.Column('bbox_y_max', sa.Float(), nullable=False),
        sa.Column('bbox_width', sa.Float(), nullable=True),
        sa.Column('bbox_height', sa.Float(), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.Column('validated', sa.String(), nullable=True, default='pending'),
        sa.Column('validated_by_id', sa.Integer(), nullable=True),
        sa.Column('notes', sa.Text(), nullable=True),
        sa.ForeignKeyConstraint(['image_id'], ['images.id'], ),
        sa.ForeignKeyConstraint(['validated_by_id'], ['users.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index('idx_detections_id', 'detections', ['id'], unique=False)
    op.create_index('idx_detections_image_id', 'detections', ['image_id'], unique=False)
    op.create_index('idx_detections_validated_by_id', 'detections', ['validated_by_id'], unique=False)


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index('idx_detections_validated_by_id', table_name='detections')
    op.drop_index('idx_detections_image_id', table_name='detections')
    op.drop_index('idx_detections_id', table_name='detections')
    op.drop_table('detections')
    op.drop_index('idx_images_uploaded_by_id', table_name='images')
    op.drop_index('idx_images_project_id', table_name='images')
    op.drop_index('idx_images_id', table_name='images')
    op.drop_table('images')
    op.drop_index('idx_projects_owner_id', table_name='projects')
    op.drop_index('idx_projects_id', table_name='projects')
    op.drop_table('projects')