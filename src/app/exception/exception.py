from fastapi import HTTPException


class NotFoundException(HTTPException):
    def __init__(self, msg: str = "not found data"):
        super().__init__(status_code=404, detail=msg)