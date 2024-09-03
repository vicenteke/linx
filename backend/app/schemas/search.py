from pydantic import BaseModel, Field, computed_field
from datetime import datetime


class SearchSchema(BaseModel):
    city: str = Field(max_length=150, description='actual city name')
    search: str = Field(max_length=150, description='search query')
    created_on: datetime = Field(description='search date', exclude=True)

    @computed_field
    def date(self) -> str:
        return str(self.created_on)
