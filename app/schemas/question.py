from datetime import datetime
from pydantic import BaseModel, Field

class QuestionBase(BaseModel):
    text: str = Field(..., min_length=10, max_length=500)

class QuestionCreate(QuestionBase):
    pass

class QuestionUpdate(QuestionBase):
    pass

class QuestionInDB(QuestionBase):
    id: int
    created_at: datetime
    responses_count: int = 0  # Default value

    class Config:
        from_attributes = True

class QuestionOut(QuestionInDB):
    pass