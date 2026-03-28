from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str
    description: str

class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    category: str
    priority: str
    user_id: int

    class Config:
        from_attributes = True  