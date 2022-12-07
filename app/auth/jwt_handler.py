# This file is responsible for signing, encoding, decoding and returning jwt
import time
import jwt

from decouple import config

JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")


def token_response(token: str):
    return {"access_token": token}


def signJWT(userID: str):
    payload = {"user_id": userID, "expiry": time.time() + 604800}

    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token_response(token)


def decodeJWT(token: str):
    try:
        decode_token = jwt.decode(token, JWT_SECRET, algorithm=JWT_ALGORITHM)
        return decode_token if decode_token["expires"] >= time.time() else None
    except Exception:
        return {}
