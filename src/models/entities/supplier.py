import uuid
from datetime import datetime ,timezone
from archipy.models.entities.sqlalchemy.base_entities import UpdatableDeletableAdminEntity
from sqlalchemy import UUID,DateTime ,String,Text
from sqlalchemy.orm import Mapped, Synonym, mapped_column



# ========================== جدول تامین کنندگان===========================

class Supplier(UpdatableDeletableAdminEntity):
    __tablename__ = "suppliers"

    id = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4,)
    pk_uuid = Synonym("id")

    name: Mapped[str] = mapped_column(String(255), nullable=False, index=True,)
    phone: Mapped[str] = mapped_column(String(20), nullable=False,)
    address: Mapped[str] = mapped_column(Text, nullable=True,)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False,)