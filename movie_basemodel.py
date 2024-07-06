from pydantic import BaseModel, Field  # base model is a package of pydantic
import datetime
from data.genre import GenreEnum
from lanuage import Language  #from 'filename' import 'classname'


class MoviebaseModel(BaseModel):
    name: str = Field(max_length=100,min_length=3,description="Name of the movie")
    genre: GenreEnum
    release_date: datetime.date
    rating: int = Field(lt=10,gt =1,description="Rating of the movie")
    language: Language
