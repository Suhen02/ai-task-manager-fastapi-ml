from fastapi.responses import JSONResponse
from app.core.logger import logger
from app.core.exceptions import AppException


async def app_exception_handler(request, exc: AppException):
    logger.error(f"AppException: {exc.message}")
    return JSONResponse(
        status_code=exc.status_code,
        content={"success": False, "error": exc.message}
    )


async def generic_exception_handler(request, exc: Exception):
    logger.exception(str(exc))
    return JSONResponse(
        status_code=500,
        content={"success": False, "error": "Internal Server Error"}
    )