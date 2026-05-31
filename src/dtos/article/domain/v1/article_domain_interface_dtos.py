from uuid import UUID
from datetime import date
from typing import Optional,List
from pydantic import Field,model_validator
from archipy.models.dtos.base_dtos import BaseDTO

from src.models.type.enum_type import UnitType,PymantType

# --------------------------------------Prodacte-------------------------------------
# -----------------------------------------------------------------------------------
class BaseSchemaProducts(BaseDTO):
    name: str = Field(..., description="نام کالا")
    barcode: Optional[str] = Field(None, description="بارکد کالا")
    purchase_price: Optional[int] = Field(None, description="قیمت خرید")
    normal_price: int = Field(..., description="قیمت عادی")
    discounted_price: int = Field(..., description="قیمت تخفیفی")
    current_stock: Optional[int] = Field(0, description="موجودی فعلی")
    unit: Optional[UnitType] = Field(UnitType.NUMBER, description="واحد")
    default_sale_unit: Optional[UnitType] = Field(UnitType.NUMBER, description="واحد پیش فرض فروش")

class ProductIdentifier(BaseDTO):
    id: Optional[UUID] = Field(None, description="شناسه یکتا")
    name: Optional[str] = Field(None, description="نام کالا")
    barcode: Optional[str] = Field(None, description="بارکد کالا")

class ProductsCreate(BaseDTO):
    name: str = Field(..., description="نام کالا (اجباری)")
    barcode: Optional[str] = Field(None, description="بارکد کالا")
    purchase_price: Optional[int] = Field(None, ge=0, description="قیمت خرید")
    normal_price: int = Field(..., ge=0, description="قیمت فروش")
    discounted_price: int = Field(..., ge=0, description="قیمت تخفیفی")
    current_stock: Optional[int] = Field(0, ge=0, description="موجود فعلی")
    unit: Optional[UnitType] = Field(UnitType.NUMBER, description="واحد کالا")
    default_sale_unit: Optional[UnitType] = Field(UnitType.NUMBER, description="واحد پیش فرض فروش")

class EditproductRequest(ProductIdentifier):
    name: Optional[str] = Field(None, description="نام کالا")
    normal_price: Optional[int] = Field(None, ge=0, description="قیمت عادی")
    discounted_price: Optional[int] = Field(None, ge=0, description="قیمت تخفیفی ")

class SearchProductRequest(BaseDTO):
    q: str = Field(..., min_length=1, description="متن جستجو(اسم کالا یا بارکد کالا)")

# ----------------------------------------supplier-------------------------------------------------
# -------------------------------------------------------------------------------------------------
class SupplierIdentifier(BaseDTO):
    id: Optional[UUID] = Field(None, description="شناسه یکتا")
    name: Optional[str] = Field(None, description="نام تامین کننده")

class CreateSuppliers(BaseDTO):
    name: str = Field(..., description="نام تامین کننده")
    phone: str = Field(..., description="تلفن تامین کننده")
    address: Optional[str] = Field(None, description="آدرس تامین کننده")

class EditSupplierRequest(SupplierIdentifier):
    name: Optional[str] = Field(None, description="نام تامین کننده")
    phone: Optional[str] = Field(None, description="تلفن تامین کننده")
    address: Optional[str] = Field(None, description="آدرس تامین کننده")

class SearchSupplierRequest(BaseDTO):
    q: str = Field(..., min_length=1, description="متن جستجو (نام تامین کننده)")

# ---------------------------------------------saleitem-------------------------------------------
class SaleItemCreateRequest(BaseDTO):
    name: Optional[str] = Field(None, description="نام کالا (برای کالاهای بدون بارکد)")
    barcode: Optional[str] = Field(None, description="بارکد کالا")
    quantity: float = Field(..., gt=0, description="تعداد (عدد/کیلو/لیتر)")

class SaleItemUpdateRequest(BaseDTO):
    quantity: Optional[float] = Field(None, gt=0, description="تعداد جدید")
    discounted_price: Optional[int] = Field(None, gt=0, description="قیمت تخفیفی جدید (ریال)")

class SaleInvoiceCreateRequest(BaseDTO):
    items: List[SaleItemCreateRequest] = Field(..., min_length=1, description="لیست کالاهای فروخته شده")
    discount_amount: int = Field(0, ge=0, description="مبلغ تخفیف کل فاکتور")
    payment_type: PymantType = Field(PymantType.CASH, description="نوع پرداخت")
    sale_date: Optional[date] = Field(None, description="تاریخ فروش (پیش‌فرض امروز)")

class SaleInvoiceUpdateRequest(BaseDTO):
    sale_date: Optional[date] = Field(None, description="تاریخ فروش جدید")
    discount_amount: Optional[int] = Field(None, ge=0, description="مبلغ تخفیف جدید")
    payment_type: Optional[PymantType] = Field(None, description="نوع پرداخت جدید")

# ---------------------------purchaseitem---------------------------------------------------------
# -------------------------------------------------------------------------------------------------
class PurchaseItemCreateRequest(BaseDTO):
    name: Optional[str] = Field(None, description="نام کالا")
    barcode: Optional[str] = Field(None, description="بارکد کالا")
    quantity: float = Field(..., gt=0, description="تعداد (عدد/کیلو/)")
    unit_price: int = Field(..., gt=0, description="قیمت واحد")

    @model_validator(mode="after")
    def check_barcode_or_name(self):
        if not self.name and not self.barcode:
            raise ValueError("حداقل یکی از فیلد های بارکد یا اسم کالا باید وارد شود")
        return self

class PurchaseItemUpdateRequest(BaseDTO):
    quantity: Optional[float] = Field(None, gt=0, description="تعداد (عدد/کیلو/)")
    unit_price: Optional[int] = Field(None, gt=0, description="قیمت واحد")

class PurchaseInvoiceCreateRequest(BaseDTO):
    supplier_id: UUID = Field(..., description="شناسه تامین کننده")
    invoice_number: str = Field(..., description="شماره فاکتور")
    items: List[PurchaseItemCreateRequest] = Field(..., min_length=1, description="لیست کالاهای خریداری شده")
    discount: int = Field(0, ge=0, description="مبلغ تخفیف کل فاکتور")
    date: Optional[date] = Field(None, description="تاریخ خرید")

class UpdatePurchaseInvoiceRequest(BaseDTO):
    discount: Optional[int] = Field(None, ge=0, description="مبلغ تخفیف ")
    date: Optional[date] = Field(None, description="تاریخ خرید")

