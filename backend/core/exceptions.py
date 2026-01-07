from rest_framework.views import exception_handler

def core_exception_handler(exc, context):
    """
    Custom exception handler that ensures all error responses structure
    matches a standard format:
    {
        "status": "error",
        "code": "SOME_ERROR_CODE",
        "message": "Human readable message",
        "details": { ... }
    }
    """
    response = exception_handler(exc, context)

    if response is not None:
        custom_data = {
            "status": "error",
            "code": exc.__class__.__name__,
            "message": str(exc),
            "details": response.data
        }
        response.data = custom_data

    return response
