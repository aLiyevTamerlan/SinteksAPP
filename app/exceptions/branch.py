from app.exceptions.base import ResourceNotFoundException


class BranchNotFoundException(ResourceNotFoundException):
    def __init__(self, resource, resource_id = None, error_code = None, details = None):
        super().__init__(resource, resource_id, error_code, details)