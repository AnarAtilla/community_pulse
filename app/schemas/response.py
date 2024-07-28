from datetime import datetime
from pydantic import BaseModel

class ResponseBase(BaseModel):
    agree: bool

class ResponseCreate(ResponseBase):
    pass

class ResponseInDB(ResponseBase):
    id: int
    question_id: int
    created_at: datetime

    class Config:
        from_attributes = True

class ResponseOut(ResponseInDB):
    pass