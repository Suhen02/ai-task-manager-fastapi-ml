class AppException(Exception):
    def __init__(self, status_code: int, message: str):
        self.status_code = status_code
        self.message = message


class BadRequestException(AppException):
    def __init__(self, message="Bad request"):
        super().__init__(400, message)


class UnauthorizedException(AppException):
    def __init__(self, message="Unauthorized"):
        super().__init__(401, message)