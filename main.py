from fastapi import FastAPI

from starlette import status

from starlette.exceptions import HTTPException

from data import Movies_list

from data.genre import GenreEnum
from models.movies import MovieModel
from movie_basemodel import MoviebaseModel
from settings import initialize_db

initialize_db()
app = FastAPI()


#
#
# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
#
#
# @app.get("/hello/{rollno}")
# async def say_hello(rollno: int): #here name -argument
#     return {"message": f"Hello {rollno}"}
#
# @app.get("/Movies")  #to read data --use get()
# async def get_Movies():#it directs to the path
#     return list(Movies_list.values())
# @app.get("/Movies/{movie_name}")
#
# async def get_Movies(movie_name : str):#end point creation
#     return Movies_list[movie_name]
#
# #to get limited movies
# @app.get("/limit_Movies")
#
# async def get_Movies(offset: int, limit: int=5 ):
#     list_movies= list(Movies_list.values())
#     count=len(list_movies)                                            #For offset=3 and limit=5
#     start_index= (offset-1)*limit            #start_index=10
#     end_index= start_index+limit             #end_index=15   so movies from index 10 to 15 will get printed
#     return list_movies[start_index:end_index]
# #3.post-->Create or adding movies to existing list or taking the movies based on there genre
#
# @app.get("/add_movies")
# async def get_add_movies(genre: GenreEnum):
#     all_movies= list(Movies_list.values())
#     genre_movies= []
#     for movie in all_movies:
#         if movie['genre']== genre.value:                  #genre.value means the movie genre that is given
#             genre_movies.append(movie)
#     return genre_movies
#
# @app.get("/Addmovies")
# async def add_movies(movie: MoviebaseModel):
#     Movies_list[movie.name] = movie.dict()
#     return {"message": f'the movie {movie.name} is successfully added'}
#
# @app.get("/movies/{movie_name}")
# async def get_movies(name: str):
#     if name not in Movies_list:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Movie not found")
#     return Movies_list[name]
#
#
# @app.delete("/delete_movies/{movie_name}")
# async def delete_movies(name: str):
#     if name not in Movies_list:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found")
#     else:
#         del Movies_list[name]
#         return {"message": f'the movie {name} is successfully deleted'}
#
# @app.put("/update_movies/{movie_name}")
# async def update_movies( movie: MoviebaseModel):
#     if movie.name not in Movies_list:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found")
#     Movies_list[movie.name] =movie.model_dump()
#     return {"message": f'the movie {movie.name} is successfully updated'}
#
#
# '''@app.put("/update_movies/{movie_name}")
# async def update_movies( name :str,movie: MoviebaseModel):
#     if name not in Movies_list:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found")
# '''
# #https://docs.google.com/document/d/16kSz-H46DTU27DqmiJWUliroet4f0_JIHtSG2Izj3kM/edit?usp=sharing
#
@app.get("/movies")
async def get_all_movies():
    Movies_list = MovieModel.objects.all()
    response_list = []
    for movie in Movies_list:
        response_list.append(
            MoviebaseModel(
                name=movie.name,
                rating=movie.rating,
                release_date=movie.release_date,
                genre=movie.genre,
                language=movie.language))
    return response_list


@app.post("/create_movie")
async def create_movie(new_movie: MoviebaseModel):
    movie = MovieModel(**new_movie.model_dump())# ** is used to take data linebyline
    movie.save()
    return {"message": f"Movie {movie.name} was successfully created"}

# #it is case sensitive
# #start_index=(offset-1)*limit
# #end_index=start_index+limit
# #enum->key and values
# '''
# if horror='HORROR'
# to get 'HORROR' we should use genre.values()
# '''
# '''
# CRUD-
# C=create
# r=read
# u=update
# d=delete'''
