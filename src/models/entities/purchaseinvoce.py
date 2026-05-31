import uuid
from datetime import datetime ,timezone
from archipy.models.entities.sqlalchemy.base_entities import UpdatableDeletableAdminEntity
from sqlalchemy import UUID,Integer,DateTime ,String,text,ForeignKey
from sqlalchemy.orm import Mapped, Synonym, mapped_column



class PurchaseInvoice(UpdatableDeletableAdminEntity):
    __tablename__ = "purchase_invoices"

    id = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4,)
    pk_uuid = Synonym("id")

    invoice_number: Mapped[str] = mapped_column(String(50), nullable=False, index=True,)
    date: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=text("CURRENT_DATE"),)
    supplier_id: Mapped[str] = mapped_column(ForeignKey("suppliers.id"), nullable=False,)
    total_amount: Mapped[int] = mapped_column(Integer, nullable=True, default=0,)
    discount: Mapped[int] = mapped_column(Integer, nullable=True, default=0,)
    final_amount: Mapped[int] = mapped_column(Integer, nullable=True, default=0,)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False,)