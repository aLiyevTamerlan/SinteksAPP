from app.exceptions.base import ConflictException


class OutOfStockException(ConflictException):
    def __init__(self, message, error_code = None, details = None):
        super().__init__(
            message=message,
            error_code=error_code or "OUT_OF_STOCK",
            details=details,
        )

class InsufficientStockException(ConflictException):
    def __init__(self, message, error_code = None, details = None):
        super().__init__(
            message=message,
            error_code=error_code or "INSUFFICIENT_STOCK",
            details=details,
        )