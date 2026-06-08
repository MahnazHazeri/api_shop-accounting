from http import HTTPStatus

from archipy.models.errors import (
    AlreadyExistsError,
    InvalidArgumentError,
    NotFoundError,
    InsufficientFundsError,
    PermissionDeniedError,
    BusinessRuleViolationError,
)

from archipy.models.errors.base_error import HTTP_AVAILABLE


class NotFoundHttpError(NotFoundError):
    http_status = HTTPStatus.NOT_FOUND if HTTP_AVAILABLE else None


class RepetitiveErrorType(AlreadyExistsError):
    http_status = HTTPStatus.CONFLICT if HTTP_AVAILABLE else None


class InventoryErrorType(InsufficientFundsError):
    http_status = HTTPStatus.BAD_REQUEST if HTTP_AVAILABLE else None


class BusinessRuleHttpError(BusinessRuleViolationError):
    http_status = HTTPStatus.BAD_REQUEST if HTTP_AVAILABLE else None

class ValidationErrorType(InvalidArgumentError):
    http_status = HTTPStatus.BAD_REQUEST if HTTP_AVAILABLE else None


class TypeOfAccessError(PermissionDeniedError):
    http_status = HTTPStatus.FORBIDDEN if HTTP_AVAILABLE else None

# ----------------------------------------notfounf error------------------------------
# ------------------------------------------------------------------------------------

class ProductNotFoundError(NotFoundHttpError):
    code = "PRODUCT_NOT_FOUND"
    message_en="Product not found"
    message_fa="کالا پیدا نشد"


class SupplierNotFoundError(NotFoundHttpError):
    code = "SUPPLIER_NOT_FOUND"
    message_en = "Supplier not found"
    message_fa = "تامین کننده پیدا نشد"


class SalesInvoiceNotFoundError(NotFoundHttpError):
    code = "SALES_INVOICE_NOT_FOUND"
    message_en = "Sales invoice not found"
    message_fa = "فاکتور فروش پیدا نشد"


class PurchaseInvoiceNotFoundError(NotFoundHttpError):
    code = "PURCHASE_INVOICE_NOT_FOUND"
    message_en = "Purchase invoice not found"
    message_fa = "فاکتور خرید پیدا نشد"


class UserNotFoundError(NotFoundHttpError):
    code = "USER_NOT_FOUND"
    message_en = "User not found"
    message_fa = "کاربر پیدا نشد"


# ------------------------------------repetitive error---------------------------------
# ------------------------------------------------------------------------------------

class DuplicateInvoiceError(RepetitiveErrorType):
    code = "DUPLICATE_INVOICE_NUMBER"
    message_en = "This invoice number already exists"
    message_fa = "این شماره فاکتور قبلا ثبت شده است "


class DuplicateProductBarcodeError(RepetitiveErrorType):
    code = "DUPLICATE_PRODUCT_BARCODE"
    message_en = "This product barcode already exists"
    message_fa = "این بارکد کالا قبلا ثبت شده است "


class DuplicateUsernameError(RepetitiveErrorType):
    code = "DUPLICATE_USERNAME"
    message_en = "This username already exists"
    message_fa = "این نام کاربری قبلا ثبت شده است "

# -----------------------------------inventory error----------------------------------
# ------------------------------------------------------------------------------------

class InsufficientInventoryiError(InventoryErrorType):
    code = "INSUFFICIENT_INVENTORYI"
    message_en = "Insufficient inventory"
    message_fa = "موجودی کافی نیست"


class NegativeInventoryError(InventoryErrorType):
    code = "NEGATIVE_INVENTORY"
    message_en = "Inventory cannot be negative"
    message_fa = "موجودی نمیتواند منفی باشد"


# -----------------------------------validation error-----------------------------------
# ------------------------------------------------------------------------------------

class ProductIdentifierRequiredError(ValidationErrorType):
    code = "PRODUCT_IDENTIFIER_REQUIRED"
    message_en = "Product must have a name or barcode"
    message_fa = "کالا باید نام یا بارکد داشته باشد"

class EmptyItemListError(ValidationErrorType):
    code = "EMPTY_ITEM_LIST"
    message_en = "Item list cannot be empty"
    message_fa = "لیست آیتم ها نمی تواند خالی باشد"

class NegativeAmountError(ValidationErrorType):
    code = "NEGATIVE_AMOUNT"
    message_en = "Amount cannot be negative"
    message_fa = "مبلغ نمی تواند منفی باشد"

class NegativeQuantityError(ValidationErrorType):
    code = "NEGATIVE_QUANTITY"
    message_en = "Quantity cannot be negative"
    message_fa = "تعداد نمی تواند منفی باشد"

class NonIntegerQuantityError(ValidationErrorType):
    code = "NON_INTEGER_QUANTITY"
    message_en = "Quantity unit must be a whole number"
    message_fa = "واحد تعداد باید عدد صحیح باشد"

class InvalidUnitCombinationError(BusinessRuleHttpError):
    code = "INVALID_UNIT_COMBINATION"
    message_en = "The combination of units is not valid (e.g. quantity and package)"
    message_fa = "ترکیب واحدها معتبر نیست (مثلاً تعداد و بسته)"

class FinalAmountExceedsTotalError(BusinessRuleHttpError):
    code = "FINAL_AMOUNT_EXCEEDS_TOTAL"
    message_en = "Final amount cannot exceed the total amount"
    message_fa = "مبلغ نهایی نمی‌تواند از مبلغ کل بیشتر باشد"

# -----------------------------------access error-----------------------------------
# ------------------------------------------------------------------------------------

class NoAccessError(TypeOfAccessError):
    code = "NO_ACCESS"
    message_en = "User does not have access"
    message_fa ="کاربر دسترسی ندارد"

class InactiveUserError(TypeOfAccessError):
    code = "INACTIVE_USER"
    message_en = "The user is inactive."
    message_fa ="کاربر غیر فعال است"



