from app.schemas import HealthCheck
from datetime import datetime
from fastapi import FastAPI


app = FastAPI()


@app.get("/health", response_model=HealthCheck)
async def health_check():
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}
