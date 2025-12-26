from fastapi import FastAPI
from app.api.v1.health import health_router

app = FastAPI(title="Task Manager API", version="1.0.0")
app.include_router(health_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Task Manager API", "docs": "/docs"}
