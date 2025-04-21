from sqlmodel import SQLModel, Field

class MLModel(SQLModel, table = True):
    id: int = Field(default=None, primary_key=True)
    model_name: str
    filename: str
    description: str