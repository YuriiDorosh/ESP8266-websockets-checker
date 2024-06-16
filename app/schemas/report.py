from pydantic import BaseModel, Field
from datetime import date
from typing import Optional
import uuid

class ResponseCreateInSchema(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, description="response id")
    signal_strength: int
    mac_address: Optional[str] = None
    created_at: date = Field(
        default_factory=date.today, description="Response create date"
    )

    class Config:
        from_attributes = True 