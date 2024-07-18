import json
from fastapi import HTTPException, APIRouter, status, Depends
from datetime import datetime
import jwt
from fastapi.security import OAuth2PasswordBearer

router = APIRouter(prefix="/api")


@router.post("/join")
async def join_service(params: dict) -> dict:
    print("/join -> ",params)
    token: str = jwt.encode(params,"secret_key",algorithm="HS256")
    print("token ->",token)
    return {"status":"success", "token":token, "type":"Bearer"}


# OAuth2
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="")
@router.post("/token")
async def token_test(token: str = Depends(oauth2_scheme)) -> dict:
    print("token receive", token)
    payload = jwt.decode(token,"secret_key","HS256")
    print("payload ->", payload)
    return {"status":"success"}