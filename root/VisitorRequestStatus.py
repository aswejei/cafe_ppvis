from enum import Enum


class VisitorRequestStatus(Enum):
    SUCCESS = 'SUCCESS'
    NEED_PREPARE = 'NEED_PREPARE'
    PRODUCT_MISSING = 'PRODUCT_MISSING'
