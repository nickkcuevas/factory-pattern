"""
Main FastAPI application.
"""
from fastapi import FastAPI
from app.api import router
import uvicorn

app = FastAPI(
    title="Notification System",
    description="Example of Factory Pattern in Python",
    version="1.0.0"
)

app.include_router(router)

@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "message": "Notification System API",
        "endpoints": {
            "send": "/notifications/send",
            "types": "/notifications/types"
        }
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
