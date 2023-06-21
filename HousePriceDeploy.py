# Import libraries
from pydantic import BaseModel
from typing import Optional

class HousePrice(BaseModel):
    bedrooms : int
    bathrooms: int
    toilets: int
    title: int
    town: int
    state: int