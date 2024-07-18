from fastapi import FastAPI
import uvicorn
from backend.src.router import loginRouter
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(loginRouter.router)

origins = [
    "https://4zvty3.csb.app",
    "http://10.10.27.18:8000",  # 서버 도메인
    # 필요한 다른 도메인 추가
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == '__main__':
    uvicorn.run("main:app",host="0.0.0.0",port=8000)