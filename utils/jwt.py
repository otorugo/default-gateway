from datetime import datetime, timedelta
from enum import Enum

from jose import jwt, ExpiredSignatureError, JWTError

from constants import SECRET_KEY, ALG, EXPIRATION_TIME


class TokenStatus(Enum):
    VALID = "VALID"
    EXPIRED = "EXPIRED"
    INVALID = "INVALID"


def create_acess_token(data: dict) -> str:
    to_encode = data.copy()

    expire = datetime.now() + timedelta(minutes=EXPIRATION_TIME)

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, ALG)

    return encoded_jwt


def decode_acess_token(token: str = None) -> dict:
    payload = {}
    try:
        payload = jwt.decode(token, key=SECRET_KEY, algorithms=ALG)
        return payload.update({"token_status": TokenStatus.VALID.value})
    except ExpiredSignatureError:
        return payload.update({"token_status": TokenStatus.EXPIRED.value})
    except JWTError:
        return payload.update({"token_status": TokenStatus.INVALID.value})
