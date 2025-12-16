class ApiError(Exception):
    def __init__(self, code: str, message:str, status:int):
        self.code = code
        self.message = message
        self.status = status
        super().__init__(self.message)

    @staticmethod
    def error_response(err: Exception):
        if isinstance(err, ApiError):
            return {
                "code": err.code,
                "message": err.message,
                "status": err.status
            }
        else:
            return {
                "code": "UNKNOWN_ERROR",
                "message": "An unknown error occurred",
                "status": 500
            }
