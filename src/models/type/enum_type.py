from enum import Enum


class PymantType(str, Enum):
    CASH = "نقدی"
    CART = "کارت"



class UnitType(str, Enum):
    NUMBER = "عدد"
    KILOGRAM = "کیلو"
    PACK = "بسته"


class WarehouseType(str , Enum):
    SHOPPING = "خرید"
    SALSE = "فروش"


class RoleType(str, Enum):
    ADMIN = "مدیر"
    CASHIER ="صندوقدار"
    ACCOUNTANT="حسابدار"

