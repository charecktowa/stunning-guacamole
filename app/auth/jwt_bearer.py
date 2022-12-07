# The function of this file is to check whether the request is authorized
from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from auth.jwt_handler import decodeJWT


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(
            JWTBearer, self
        ).__call__(request)

        if not credentials:
            raise HTTPException(status_code=403, detail="Tokén inválido")
        if credentials.scheme != "Bearer":
            raise HTTPException(
                status_code=HTTPException.HTTP_UNAUTHORIZED,
                detail="Tokén inválido",
            )
        return credentials.credentials

    def verify_jwt(self, jwtoken: str):
        payload = decodeJWT(jwtoken)
        return bool(payload)
