from enum import Enum


class PymantType(str, Enum):
    CASH = "نقدی"
    CART = "کارت"
    VOUCHER = "کالابرگ"


class UnitType(str, Enum):
    NUMBER = "عدد"
    KILOGRAM = "کیلو"


class WarehouseType(str , Enum):
    SHOPPING = "خرید"
    SALSE = "فروش"
