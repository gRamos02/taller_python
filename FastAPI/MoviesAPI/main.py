from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Optional

app = FastAPI()
app.title = "Mi aplicacion con FASTAPI"
app.version = "0.0.1"

class Movie(BaseModel):
    id: Optional[int] = None
    title: str
    overview: str
    year: int
    rating: float
    category: str

movies = [
    {
        'id': 1,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'    
    },
    {
        'id': 2,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'    
    },
    {
        'id': 3,
        'title': 'The notebook',
        'overview': "Una relacion toxica que no se arma.",
        'year': '2004',
        'rating': 7.8,
        'category': 'Romance'
    } 
]

@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>Hola, Bienvenido</h1>')

@app.get('/movies', tags=['movies'])
def get_movies():
    return movies

@app.get('/movies/{id}', tags=['movies']) #Parametros de ruta
def get_movie(id: int):
    for item in movies:
        if item['id'] == id:
            return item 
    return {}

@app.get('/movies/',tags=['movies']) #query
def get_movie_by_category(category:str):
    return [movie for movie in movies if movie['category'] == category]

#metodo POST
@app.post('/movies',tags=['movies'])
def create_movie(movie: Movie):
    movies.append(movie)
    return movies

#metodo PUT
@app.put('/movies/{id}',tags=['movies'])
def update_movie(id:int, movie: Movie):
    for item in movies:
        if item['id'] == id:
            item['title'] = movie.title
            item['overview'] = movie.overview
            item['year'] = movie.year
            item['rating'] = movie.rating
            item['category'] = movie.category
            return movies

#metodo DELETE
@app.delete('/movies/{id}', tags=['movies'])
def delete_movie(id:int):
    for item in movies:
        if item['id'] == id:
            movies.remove(item)
            return movies