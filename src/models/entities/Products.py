import uuid
from datetime import datetime,timezone
from archipy.models.entities.sqlalchemy.base_entities import UpdatableDeletableAdminEntity
from sqlalchemy import UUID,Integer,String,Enum as TYPEEnum,text,DateTime
from sqlalchemy.orm import Mapped, Synonym, mapped_column

from src.models.type.enum_type import UnitType


# ======================کالاها=====================

class Products(UpdatableDeletableAdminEntity):
    __tablename__ = "products"

    id = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4,)
    pk_uuid = Synonym("id")

    name: Mapped[str] = mapped_column(String(255), nullable=False, index=True,)
    barcode: Mapped[str] = mapped_column(String(50), nullable=True, index=True,)
    purchase_price: Mapped[int] = mapped_column(Integer, nullable=False,)
    normal_price: Mapped[int] = mapped_column(Integer, nullable=False,)
    discounted_price: Mapped[int] = mapped_column(Integer, nullable=False,)
    current_stock: Mapped[int] = mapped_column(Integer, nullable=True, server_default=text("0"),)
    unit: Mapped[UnitType] = mapped_column(TYPEEnum, default=UnitType.NUMBER,)
    default_sale_unit: Mapped[str] = mapped_column(TYPEEnum, default=UnitType.NUMBER,)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False,)

