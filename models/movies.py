from mongoengine import Document, StringField, EnumField, DateField, FloatField
from data.genre import GenreEnum
from lanuage import Language


class MovieModel(Document):
    meta = {"collection": "movies"}
    name = StringField(required=True, unique=True, max_length=50, min_length=3)
    genre = EnumField(GenreEnum, required=True)
    release_date = DateField(required=True)
    rating = FloatField(required=True, min_value=1.0, max_value=10.0)
    language = EnumField(Language, required=True)
