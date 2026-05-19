from app.exceptions.base import ResourceNotFoundException, ValidationException


class ProductNotFoundException(ResourceNotFoundException):
    def __init__(self, resource, resource_id = None, error_code = None, details = None):
        super().__init__(resource, resource_id, error_code, details)


class ProductBrandMismatchException(ValidationException):
    def __init__(self, message, error_code = None, details = None):
        super().__init__(
            message=message,
            error_code=error_code or "PRODUCT_BRAND_MISMATCH",
            details=details,
        )

class ProductNotAvailableInBranchException(ResourceNotFoundException):
    def __init__(self, message, error_code = None, details = None):
        super().__init__(
            resource="Product",
            resource_id=None,
            error_code=error_code or "PRODUCT_NOT_AVAILABLE_IN_BRANCH",
            details=details,
        )