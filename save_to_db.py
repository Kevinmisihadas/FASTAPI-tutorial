from data import Movies_list
from data.genre import GenreEnum
from lanuage import Language
from models.movies import MovieModel
from settings import initialize_db

initialize_db()

movies = list(Movies_list.values())
for movie in movies:
    movie["language"] = Language[movie["language"]]
    movie["genre"] = GenreEnum[movie["genre"]]
    MovieModel(**movie).save()
