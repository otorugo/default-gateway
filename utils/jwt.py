from datetime import datetime, timedelta, timezone
from enum import Enum

from jose import jwt, ExpiredSignatureError, JWTError

from constants import SECRET_KEY, ALG, EXPIRATION_TIME


class TokenStatus(Enum):
    VALID = "VALID"
    EXPIRED = "EXPIRED"
    INVALID = "INVALID"


def create_acess_token(data: dict) -> str:
    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(minutes=EXPIRATION_TIME)

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, ALG)

    return encoded_jwt


def decode_acess_token(token: str = None) -> dict:
    payload = {}
    try:
        payload = jwt.decode(token, key=SECRET_KEY, algorithms=ALG)
        payload.update({"token_status": TokenStatus.VALID.value})
        return payload
    except ExpiredSignatureError:
        payload.update({"token_status": TokenStatus.EXPIRED.value})
        return payload
    except JWTError:
        payload.update({"token_status": TokenStatus.INVALID.value})
        return payload


if __name__ == '__main__':
    my_acess = {
        "name": "torugo",
        "email": "victorsilva698@gmail.com"
    }
    token = create_acess_token(my_acess)

    result = decode_acess_token(token)
    print(result)
