from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from archipy.models.errors import (
    AlreadyExistsError,
    InvalidArgumentError,
    NotFoundError,
    InsufficientFundsError,
    PermissionDeniedError,
    BusinessRuleViolationError,
)


def register_exception_handlers(app: FastAPI) -> None:

    @app.exception_handler(AlreadyExistsError)
    async def handle_already_exists(request: Request, exc: AlreadyExistsError):
        return JSONResponse(
            status_code= exc.http_status or 409,
            content = exc.to_dict()
        )



    @app.exception_handler(InvalidArgumentError)
    async def handle_invalid_argument(request: Request, exc: InvalidArgumentError):
        return JSONResponse(
            status_code= exc.http_status or 400,
            content = exc.to_dict()
        )


    @app.exception_handler(NotFoundError)
    async def handle_not_found(request: Request, exc: NotFoundError):
        return JSONResponse(
            status_code= exc.http_status or 404,
            content = exc.to_dict()
        )


    @app.exception_handler(InsufficientFundsError)
    async def handle_insufficient_funds(request: Request, exc: InsufficientFundsError):
        return JSONResponse(
            status_code= exc.http_status or 400,
            content = exc.to_dict()
        )


    @app.exception_handler(PermissionDeniedError)
    async def handle_permission_denied(request: Request, exc: PermissionDeniedError):
        return JSONResponse(
            status_code= exc.http_status or 403,
            content = exc.to_dict()
        )


    @app.exception_handler(BusinessRuleViolationError)
    async def handle_business_rule_violation(request: Request, exc: BusinessRuleViolationError):
        return JSONResponse(
            status_code= exc.http_status or 400,
            content = exc.to_dict()
        )





