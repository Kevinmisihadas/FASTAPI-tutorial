from fastapi import FastAPI

from data import Movies_list


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{rollno}")
async def say_hello(rollno: int): #here name -argument
    return {"message": f"Hello {rollno}"}

@app.get("/Movies")  #to read data --use get()
async def get_Movies():#it directs to the path
    return list(Movies_list.values())
@app.get("/Movies/{movie_name}")

async def get_Movies(movie_name : str):#end point creation
    return Movies_list[movie_name]

#to get limited movies
@app.get("/limit_Movies")

async def get_Movies(offset: int, limit: int=5 ):
    list_movies= list(Movies_list.values())
    count=len(list_movies)                                            #For offset=3 and limit=5
    start_index= (offset-1)*limit            #start_index=10
    end_index= start_index+limit             #end_index=15   so movies from index 10 to 15 will get printed
    return list_movies[start_index:end_index]
#3.post-->Create or adding movies to existing list or taking the movies based on there genre

@app.get("/add_movies")
async def get_add_movies(genre: GenreEnum):
    all_movies= list(Movies_list.values())
    genre_movies= []
    for movie in all_movies:
        if movie['genre']== genre.values:
            genre_movies.append(movie)
    return genre_movies

#




#it is case sensitive
#start_index=(offset-1)*limit
#end_index=start_index+limit
#enum->key and values
'''
if horror='HORROR'
to get 'HORROR' we should use genre.values()
'''
'''
CRUD-
C=create
r=read
u=update
d=delete'''
