import uvicorn
from fastapi import FastAPI
# 1. 务必先加载环境变量
from dotenv import load_dotenv
load_dotenv() 

# 2. 然后再导入你的路由（因为路由里初始化了 Agent）
from app.api.routes import router

app = FastAPI(title="Lightweight Agent System API")
app.include_router(router, prefix="/v1")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)