import uuid
from datetime import datetime ,timezone
from archipy.models.entities.sqlalchemy.base_entities import UpdatableDeletableAdminEntity
from sqlalchemy import UUID,Integer,DateTime,ForeignKey
from sqlalchemy.orm import Mapped, Synonym, mapped_column



# ======================= جدول آیتم ها فروش===========================

class SaleItem(UpdatableDeletableAdminEntity):
    __tablename__ = "sales_items"

    id = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4,)
    pk_uuid = Synonym("id")

    sales_invoice_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("sales_invoices.id", ondelete="CASCADE"), nullable=False,)
    product_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("products.id"), nullable=False,)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False,)
    market_price: Mapped[int] = mapped_column(Integer, nullable=False,)
    discounted_price: Mapped[int] = mapped_column(Integer, nullable=False,)
    total_price: Mapped[int] = mapped_column(Integer, nullable=False,)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False,)