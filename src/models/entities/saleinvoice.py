import uuid
from datetime import datetime ,timezone
from archipy.models.entities.sqlalchemy.base_entities import UpdatableDeletableAdminEntity
from sqlalchemy import UUID,Integer,DateTime ,String,text,ForeignKey
from sqlalchemy.orm import Mapped, Synonym, mapped_column
from sqlalchemy import Enum as TYPEEnum

from src.models.type.enum_type import  PymantType



# =======================جدول فاکتور فروش=======================

class SaleInvoice(UpdatableDeletableAdminEntity):
    __tablename__ = "sales_invoices"

    id = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4 ,)
    pk_uuid = Synonym("id")

    invoice_number: Mapped[str] = mapped_column(String(50), nullable=False, index=True ,)
    sale_date: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=text("CURRENT_DATE") ,)
    users_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"), nullable=False,)
    total_amount: Mapped[int] = mapped_column(Integer, nullable=True, default=0 ,)
    discount_amount: Mapped[int] = mapped_column(Integer, nullable=True, default=0 ,)
    final_amount: Mapped[int] = mapped_column(Integer, nullable=True, default=0 ,)
    payment_type: Mapped[PymantType] = mapped_column(TYPEEnum ,default=PymantType.CASH ,nullable=True ,)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False ,)
