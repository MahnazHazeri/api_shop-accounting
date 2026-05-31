from uuid import UUID
from datetime import datetime,date
from pydantic import Field
from typing import Optional,List
from archipy.models.dtos.base_dtos import BaseDTO


from src.models.type.enum_type import PymantType
from src.dtos.article.domain.v1.article_domain_interface_dtos import (
    BaseSchemaProducts,
    ProductIdentifier,
    SupplierIdentifier,
)



# ---------------------------------------product-----------------------------------------------
# ---------------------------------------------------------------------------------------------
class GetListProducts(BaseSchemaProducts):
    id: UUID = Field(..., description="شناسه یکتا")
    created_at: datetime = Field(..., description="تاریخ ایجاد")

class GetDetailsProduct(BaseSchemaProducts):
    id: UUID = Field(..., description="شناسه یکتا")
    created_at: datetime = Field(..., description="تاریخ ایجاد")

class DeleteProductRequest(ProductIdentifier):
    pass

class DeleteProductsResponse(BaseDTO):
    message: str = Field(..., description="کالا با موفقیت حذف شد")

class EditproductResponse(BaseSchemaProducts):
    pass

class SearchProductResponse(BaseSchemaProducts):
    id: UUID = Field(..., description="شناسه یکتا")
    created_at: datetime = Field(..., description="تاریخ ایجاد")

# ---------------------------supplier--------------------------------------------------------
# -------------------------------------------------------------------------------------------
class BaseSupplierResponse(BaseDTO):
    id: UUID = Field(..., description="شناسه یکتا")
    name: str = Field(..., description="نام تامین کننده")
    phone: Optional[str] = Field(None, description="تلفن تامین کننده")
    address: Optional[str] = Field(None, description="آدرس تامین کننده")
    created_at: datetime = Field(..., description="تاریخ ایجاد")

class EditSupplierResponse(BaseDTO):
    message: str = Field(..., description="تغییرات به درستی ثبت شد")
    supplier: BaseSupplierResponse = Field(..., description="اطلاعات تامین کننده پس از ویرایش")

class SupplierDetailsResponse(BaseSupplierResponse):
    pass

class DeleteSupplierRequest(SupplierIdentifier):
    pass

class DeleteSupplierResponse(BaseDTO):
    message: str = Field(..., description="اطلاعات تامین کننده به درستی حذف شدند")

class GetSupplierList(BaseDTO):
    id: UUID = Field(..., description="شناسه یکتا")
    name: str = Field(..., description="نام تامین کننده")

class SearchSupplierResponse(BaseSupplierResponse):
    pass

# -------------------------------------saleitem-response----------------------------------
# ----------------------------------------------------------------------------------------
class SaleItemResponse(BaseDTO):
    id: UUID = Field(..., description="شناسه آیتم")
    product_id: UUID = Field(..., description="شناسه کالا")
    product_name: str = Field(..., description="نام کالا")
    barcode: str = Field(..., description="بارکد کالا")
    quantity: float = Field(..., description="تعداد")
    unit: str = Field(..., description="واحد")
    market_price: int = Field(..., description="قیمت بازار")
    discounted_price: int = Field(..., description="قیمت تخفیفی")
    total_price: int = Field(..., description="قیمت کل")

class SaleItemUpdateResponse(SaleItemResponse):
    pass

class SaleItemDetailResponse(SaleItemResponse):
    pass

class SaleItemListResponse(BaseDTO):
    total: int = Field(..., description="تعداد کل آیتم ها")
    items: List[SaleItemResponse] = Field(..., description="لیست آیتم ها")

class SaleInvoiceResponse(BaseDTO):
    id: UUID = Field(..., description="شناسه فاکتور")
    invoice_number: str = Field(..., description="شماره فاکتور")
    sale_date: date = Field(..., description="تاریخ فروش")
    total_amount: int = Field(..., description="جمع کل (قیمت بازار × تعداد)")
    discount_amount: int = Field(..., description="مبلغ تخفیف")
    final_amount: int = Field(..., description="مبلغ نهایی")
    payment_type: PymantType = Field(..., description="نوع پرداخت")
    created_at: datetime = Field(..., description="تاریخ ایجاد")
    items: List[SaleItemResponse] = Field(..., description="لیست کالاهای فروخته شده")

class SaleInvoiceUpdateResponse(BaseDTO):
    message: str = Field("فاکتور فروش با موفقیت ویرایش شد", description="پیام نتیجه عملیات")
    invoice: SaleInvoiceResponse = Field(..., description="اطلاعات کامل فاکتور پس از ویرایش")

class DeleteSaleInvoiceResponse(BaseDTO):
    message: str = Field("فاکتور فروش با موفقیت حذف شد", description="پیام نتیجه عملیات")
    deleted_id: UUID = Field(..., description="شناسه فاکتور حذف شده")
    invoice_number: str = Field(..., description="شماره فاکتور حذف شده")

class SaleInvoiceDetailResponse(SaleInvoiceResponse):
    pass

class SaleInvoiceListResponse(BaseDTO):
    total: int = Field(..., description="تعداد کل فاکتور ها")
    item: List[SaleInvoiceResponse] = Field(..., description="لیست فاکتور ها")

# ---------------------------purchaseitem---------------------------------------------------
# ------------------------------------------------------------------------------------------
class PurchaseItemCreateResponse(BaseDTO):
    id: UUID = Field(..., description="شناسه آیتم")
    purchase_invoice_id: UUID = Field(..., description="شناسه فاکتور خرید")
    product_id: UUID = Field(..., description="شناسه کالا")
    product_name: str = Field(..., description="نام کالا")
    barcode: Optional[str] = Field(None, description="بارکد کالا")
    quantity: float = Field(..., description="تعداد")
    unit: str = Field(..., description="واحد")
    unit_price: int = Field(..., description="قیمت واحد")
    total_price: int = Field(..., description="قیمت کل")
    created_at: datetime = Field(..., description="تاریخ ایجاد")

class PurchaseItemUpdateResponse(BaseDTO):
    message: str = Field("آیتم خرید با موفقیت ویرایش شد", description="پیام نتیجه عملیات")
    item: PurchaseItemCreateResponse = Field(..., description="خروجی ویرایش شده به صورت کامل")

class PurchaseItemDeleteResponse(BaseDTO):
    message: str = Field("آیتم خرید با موفقیت حذف شد", description="پیام نتیجه عملیات")

class PurchaseItemDetailResponse(PurchaseItemCreateResponse):
    pass

class PurchaseInvoiceSchema(BaseDTO):
    id: UUID = Field(..., description="شناسه فاکتور")
    invoice_number: str = Field(..., description="شماره فاکتور")
    date: date = Field(..., description="تاریخ خرید")
    supplier_id: UUID = Field(..., description="شناسه تامین‌کننده")
    supplier_name: str = Field(..., description="نام تامین‌کننده")
    total_amount: int = Field(..., description="جمع کل (قیمت واحد × تعداد)")
    discount: int = Field(..., description="تخفیف (ریال)")
    final_amount: int = Field(..., description="مبلغ نهایی (ریال)")
    created_at: datetime = Field(..., description="تاریخ ایجاد")
    items: List[PurchaseItemCreateResponse] = Field(..., description="لیست کالاهای خریداری شده")

class PurchaseInvoiceCreateResponse(PurchaseInvoiceSchema):
    message: str = Field("فاکتور خرید با موفقیت ایجاد شد", description="پیام نتیجه عملیات")

class UpdatePurchaseInvoiceResponse(BaseDTO):
    message: str = Field("فاکتور خرید اصلاح شد", description="پیام نتیجه عملیات")
    invoice: PurchaseInvoiceSchema = Field(..., description="اطلاعات کامل فاکتور پس از اصلاح")

class DeletePurchaseInvoiceResponse(BaseDTO):
    message: str = Field("فاکتور با موفقیت حذف شد", description="پیام نتیجه عملیات")

class PurchaseInvoiceListRequest(BaseDTO):
    skip: int = Field(0, ge=0, description="تعداد رد شده")
    limit: int = Field(100, ge=1, le=1000, description="تعداد در هر صفحه")
    from_date: Optional[date] = Field(None, description="از تاریخ")
    to_date: Optional[date] = Field(None, description="تا تاریخ")
    supplier_id: Optional[UUID] = Field(None, description="شناسه تامین‌کننده")
    supplier_name: Optional[str] = Field(None, description="نام تامین‌کننده")

class PurchaseInvoiceListResponse(BaseDTO):
    total: int = Field(..., description="تعداد کل فاکتورها")
    items: List[PurchaseInvoiceSchema] = Field(..., description="لیست فاکتورها")

class PurchaseInvoiceDetailResponse(PurchaseInvoiceSchema):
    pass

# --------------------------------------------inventorymove-----------------------------------
# --------------------------------------------------------------------------------------------
class InventorySchema(BaseDTO):
    product_id: UUID = Field(..., description="شناسه کالا")
    product_name: str = Field(..., description="نام کالا")
    barcode: Optional[str] = Field(None, description="بارکد کالا")
    current_stock: int = Field(..., description="موجودی فعلی")
    unit: str = Field(..., description="واحد کالا")

class InventoryMovementResponse(BaseDTO):
    id: UUID = Field(..., description="شناسه حرکت")
    product_id: UUID = Field(..., description="شناسه کالا")
    product_name: str = Field(..., description="نام کالا")
    type: str = Field(..., description="نوع حرکت (purchase/sale/correction)")
    reference_id: UUID = Field(..., description="شناسه مرجع (فاکتور خرید/فروش)")
    quantity: int = Field(..., description="تعداد (مثبت=ورود، منفی=خروج)")
    stock_before: int = Field(..., description="موجودی قبل از حرکت")
    stock_after: int = Field(..., description="موجودی بعد از حرکت")
    created_at: datetime = Field(..., description="تاریخ ایجاد حرکت")

class InventoryMovementListRequest(BaseDTO):
    skip: int = Field(0, ge=0, description="تعداد رد شده")
    limit: int = Field(100, ge=1, le=1000, description="تعداد در هر صفحه")
    from_date: Optional[datetime] = Field(None, description="از تاریخ")
    to_date: Optional[datetime] = Field(None, description="تا تاریخ")
    product_id: Optional[UUID] = Field(None, description="شناسه کالا")
    type: Optional[str] = Field(None, description="نوع حرکت (purchase/sale/correction)")

class InventoryMovementListResponse(BaseDTO):
    total: int = Field(..., description="تعداد کل حرکات")
    items: List[InventoryMovementResponse] = Field(..., description="لیست حرکات")

class CurrentStockRequest(BaseDTO):
    product_id: UUID = Field(..., description="شناسه کالا")
    barcode: Optional[str] = Field(None, description="بارکد کالا")
    name: Optional[str] = Field(None, description="نام کالا")

class CurrentStockResponse(InventorySchema):
    pass

class LowStockRequest(BaseDTO):
    threshold: int = Field(10, ge=0, description="آستانه موجودی کم (حداکثر موجودی مجاز)")
    skip: int = Field(0, ge=0, description="تعداد رد شده")
    limit: int = Field(100, ge=1, le=1000, description="تعداد در هر صفحه")

class LowStockItemResponse(InventorySchema):
    threshold: int = Field(..., description="آستانه موجودی کم")

class LowStockListResponse(BaseDTO):
    total: int = Field(..., description="تعداد کل کالاها")
    items: List[LowStockItemResponse] = Field(..., description="لیست کالاها")

# -----------------------------------------dailysales--------------------------------------------------
# -----------------------------------------------------------------------------------------------------
class DailySalesReportItem(BaseDTO):
    product_name: str = Field(..., description="نام کالا")
    total_quantity: float = Field(..., description="تعداد کل فروخته شده")
    total_amount: int = Field(..., description="مبلغ کل فروش")

class DailySalesReportResponse(BaseDTO):
    date: date = Field(..., description="تاریخ گزارش")
    total_sales: int = Field(..., description="جمع کل فروش")
    invoice_count: int = Field(..., description="تعداد فاکتور ها")
    items_sold: List[DailySalesReportItem] = Field(..., description="لیست کالاهای فروخته شده")

class ProfitSchema(BaseDTO):
    from_date: Optional[date] = Field(None, description="از تاریخ")
    to_date: Optional[date] = Field(None, description="تا تاریخ")

class ProfitLossRequest(BaseDTO):
    from_date: date = Field(..., description="از تاریخ")
    to_date: date = Field(..., description="تا تاریخ")

class ProfitLossResponse(ProfitSchema):
    total_sales: int = Field(..., description="کل فروش")
    total_purchases: int = Field(..., description="کل خرید")
    gross_profit: int = Field(..., description="سود ناخالص")
    profit_margin: float = Field(..., description="درصد سود")

class TopProductsRequest(ProfitSchema):
    limit: int = Field(10, ge=1, le=100, description="تعداد نتایج")

class TopProductItemResponse(BaseDTO):
    product_id: str = Field(..., description="شناسه کالا")
    product_name: str = Field(..., description="نام کالا")
    total_quantity: int = Field(..., description="تعداد کل فروخته شده")
    total_amount: int = Field(..., description="مبلغ کل فروش")

class TopProductsResponse(ProfitSchema):
    items: List[TopProductItemResponse] = Field(..., description="لیست کالا های پر فروش")

class MonthlySalesRequest(BaseDTO):
    year: int = Field(..., ge=1300, le=1500, description="سال")
    month: Optional[int] = Field(None, ge=1, le=12, description="ماه")

class SalesReportItemResponse(BaseDTO):
    period: str = Field(..., description="دوره")
    total_sales: int = Field(..., description="کل فروش")
    invoice_count: int = Field(..., description="تعداد فاکتورها")

class MonthlySalesResponse(BaseDTO):
    year: int = Field(..., description="سال")
    reports: List[SalesReportItemResponse] = Field(..., description="گزارش‌های ماهانه/سالانه")