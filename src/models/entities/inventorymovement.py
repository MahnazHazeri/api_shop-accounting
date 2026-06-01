import uuid
from datetime import datetime ,timezone
from archipy.models.entities.sqlalchemy.base_entities import UpdatableDeletableAdminEntity
from sqlalchemy import UUID,String,Integer,DateTime,ForeignKey
from sqlalchemy.orm import Mapped, Synonym, mapped_column
from sqlalchemy import Enum as TYPEEnum

from src.models.type.enum_type import WarehouseType



# ======================== جدول حرکات انبار========================

class InventoryMovement(UpdatableDeletableAdminEntity):
    __tablename__ = "inventory_movements"

    id = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4,)
    pk_uuid = Synonym("id")

    product_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("products.id"), nullable=False,)
    type: Mapped[WarehouseType] = mapped_column(TYPEEnum,nullable=False)
    reference_id: Mapped[str] = mapped_column(String(36), nullable=False,)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False,)
    stock_before: Mapped[int] = mapped_column(Integer, nullable=False,)
    stock_after: Mapped[int] = mapped_column(Integer, nullable=False,)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False,)