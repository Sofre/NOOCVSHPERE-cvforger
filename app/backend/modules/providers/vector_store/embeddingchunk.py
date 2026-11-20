
import uuid

from sqlalchemy import String, Text, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from pgvector.sqlalchemy import VECTOR

from app.infrastructure.database.base import Base


class EmbeddingChunk(Base):
    __tablename__ = "embedding_chunks"

    # Primary key
    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    # Source identification
    source_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    source_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        nullable=False
    )

    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        nullable=False,
        index=True
    )

    # Original text
    content: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    # Vector representation
    embedding: Mapped[list[float]] = mapped_column(
        VECTOR(384),
        nullable=False
    )

    # Chunk information
    section: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    chunk_index: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    # Embedding model identification
    embedding_model: Mapped[str] = mapped_column(
        String(150),
        nullable=False
    )
