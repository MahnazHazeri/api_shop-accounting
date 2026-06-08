import uuid
from datetime import datetime ,timezone
from archipy.models.entities.sqlalchemy.base_entities import UpdatableDeletableAdminEntity
from sqlalchemy import UUID,text,Integer,DateTime,ForeignKey
from sqlalchemy.orm import Mapped, Synonym, mapped_column
from sqlalchemy import Numeric,Enum as TYPEEnum

from src.models.type.enum_type import WarehouseType,UnitType



# ======================== جدول حرکات انبار========================

class InventoryMovement(UpdatableDeletableAdminEntity):
    __tablename__ = "inventory_movements"

    id = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4,)
    pk_uuid = Synonym("id")

    product_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("products.id"), nullable=False,)
    type: Mapped[WarehouseType] = mapped_column(TYPEEnum,nullable=False,)
    reference_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False,)
    quantity: Mapped[float] = mapped_column(Numeric(asdecimal=False), nullable=False,)
    stock_before: Mapped[float] = mapped_column(Numeric(asdecimal=False), nullable=False,)
    stock_after: Mapped[float] = mapped_column(Numeric(asdecimal=False), nullable=False,)
    selected_unit: Mapped[UnitType] = mapped_column(TYPEEnum, nullable=False,)
    conversion_factor: Mapped[int] = mapped_column(Integer, nullable=False, server_default=text("1"),)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False,)


