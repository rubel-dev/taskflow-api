


from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from app.core.security import ALGORITHM, SECRET_KEY
from jose import JWTError, jwt

security = HTTPBearer()
def get_current_user(
        credentials: HTTPAuthorizationCredentials = Depends(security)
):
    token = credentials.credentials
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms = [ALGORITHM]
        )
        user_id = payload.get('user_id')
        if user_id is None:
            raise HTTPException(
                status_code=401,
                detail='Invalid token'
            )
        return user_id
    except JWTError:
        raise HTTPException(
            status_code=401,
            detail = 'Invalid token'
        )