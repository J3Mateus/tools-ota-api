from rest_framework import status

class ApplicationError(Exception):
    def __init__(self, message = "Internal Server Error", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, extra=None):
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.extra = extra or {}

class APIExternalError(ApplicationError):
    def __init__(self, message, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, extra=None):
        super().__init__(message, status_code, extra)
        self.message = message
        self.status_code = status_code
        self.extra = extra or {}

class NotFoundError(ApplicationError):
    def __init__(self, message = "Resource Not Found", status_code=status.HTTP_404_NOT_FOUND,extra=None):
        super().__init__(message,status_code,extra)
        self.message = message
        self.status_code = status_code
        self.extra = extra or {}

class DuplicateResourceError(ApplicationError):
    def __init__(self, message="Resource already exists", status_code=status.HTTP_409_CONFLICT, extra=None):
        super().__init__(message, status_code, extra)
        self.message = message
        self.status_code = status_code
        self.extra = extra or {}

class AttributeNotFoundError(AttributeError):
    def __init__(self, message="Attribute not found",status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,extra=None):
        super().__init__(message,status_code,extra)
        self.message = message
        self.status_code = status_code
        self.extra = extra or {}

class UpdateError(ApplicationError):
    def __init__(self, message="Entity not update", status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, extra=None):
        super().__init__(message, status_code, extra)
        self.message = message
        self.status_code = status_code
        self.extra = extra or {}

class ForbiddenError(ApplicationError):
    def __init__(self, message="Action Forbidden", status_code=status.HTTP_403_FORBIDDEN, extra=None):
        super().__init__(message, status_code, extra)
        self.message = message
        self.status_code = status_code
        self.extra = extra or {}

class TooManyRequestsError(ApplicationError):
    def __init__(self, message="Too many requests, limit reached", status_code=status.HTTP_429_TOO_MANY_REQUESTS, extra=None):
        super().__init__(message, status_code, extra)
        self.message = message
        self.status_code = status_code
        self.extra = extra or {}

class BadRequestError(ApplicationError):
    def __init__(self, message="Bad Request", status_code=status.HTTP_400_BAD_REQUEST, extra=None):
        super().__init__(message, status_code, extra)
        self.message = message
        self.status_code = status_code
        self.extra = extra or {}

class ForbiddenError(ApplicationError):
    def __init__(self, message="Action Forbidden", status_code=status.HTTP_403_FORBIDDEN, extra=None):
        super().__init__(message, status_code, extra)
        self.message = message
        self.status_code = status_code
        self.extra = extra or {}