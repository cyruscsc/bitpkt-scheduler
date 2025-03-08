from pydantic import BaseModel


class HealthCheck(BaseModel):
    status: str
    timestamp: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {"status": "healthy", "timestamp": "2025-03-08T12:00:00.000000"}
            ]
        }
    }
