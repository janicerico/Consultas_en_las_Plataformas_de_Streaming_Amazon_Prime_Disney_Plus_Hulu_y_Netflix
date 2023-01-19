# Importación de las librerías a utilizar
from fastapi import FastAPI
import pandas as pd

app = FastAPI   (title = 'Api para Consultar Datos de Plataformas de Streaming',
                 description = 'Amazon Prime, Disney Plus, Hulu, Netflix',)


# Se carga la base de datos que contiene todas las tablas unificadas
df_all_streaming = pd.read_csv('Datasets/all_streaming.csv')


# Información del proyecto
@app.get('/')
async def index():
    return 'Proyecto Individual 01 de Data Engineer - Por Janice Rico'


# Información de la API
@app.get('/about')
async def about():
    return 'Esta API fue creada con FastAPI y Uvicorn'


# 1. Calcular la cantidad de veces que aparece una keyword en el título de peliculas/series, por plataforma
@app.get('/1- get_word_count')
async def get_word_count (platform:str, keyword:str):
    if platform == 'amazon':
        df_Amazon = df_all_streaming[df_all_streaming.id.str.startswith('a')]
        cantidad = len(df_Amazon[df_Amazon['title'].str.contains(keyword)])
        return platform, cantidad
    if platform == 'disney':
        df_Disney = df_all_streaming[df_all_streaming.id.str.startswith('d')]
        cantidad = len(df_Disney[df_Disney['title'].str.contains(keyword)])
        return platform, cantidad
    if platform == 'hulu':
        df_Hulu = df_all_streaming[df_all_streaming.id.str.startswith('h')]
        cantidad = len(df_Hulu[df_Hulu['title'].str.contains(keyword)])
        return platform, cantidad
    if platform == 'netflix':
        df_Netflix = df_all_streaming[df_all_streaming.id.str.startswith('n')]
        cantidad = len(df_Netflix[df_Netflix['title'].str.contains(keyword)])
        return platform, cantidad


# 2. Calcular cantidad de Películas por Plataforma, con un Puntaje mayor a XX, en determinado Año
@app.get('/2- get_score_count')
async def get_score_count (platform:str, score:int, year:int):
    cantidad = len(df_all_streaming[(df_all_streaming['release_year'] == year) & (df_all_streaming['score'] > score) & (df_all_streaming.id.str.startswith(platform[0])) & (df_all_streaming['type'] == 'movie')])
    return platform, cantidad


# 3. Mostrar la segunda película con mayor score para una plataforma determinada,
# según el orden alfabético de los títulos.
@app.get('/3- get_second_score')
async def get_second_score (platform:str):
    if platform == 'amazon':
        new_df = df_all_streaming[df_all_streaming.id.str.startswith('a')]
    if platform == 'disney':
        new_df = df_all_streaming[df_all_streaming.id.str.startswith('d')]
    if platform == 'hulu':
        new_df = df_all_streaming[df_all_streaming.id.str.startswith('h')]
    if platform == 'netflix':
        new_df = df_all_streaming[df_all_streaming.id.str.startswith('n')]
    new_df = new_df.sort_values(by=['score','title'], ascending=[False,True])
    new_df = new_df.reset_index(drop=True)
    new_title = new_df['title'][1]
    new_score = new_df['score'][1]
    return new_title, str(new_score)


# 4. Calcular la Película que más duró según Año, Plataforma y Tipo de duración
@app.get('/4- get_longest')
async def get_longest (platform:str, duration_type:str, year:int):
    if platform == 'amazon':
        new_df = df_all_streaming[df_all_streaming.id.str.startswith('a')]
    if platform == 'disney':
        new_df = df_all_streaming[df_all_streaming.id.str.startswith('d')]
    if platform == 'hulu':
        new_df = df_all_streaming[df_all_streaming.id.str.startswith('h')]
    if platform == 'netflix':
        new_df = df_all_streaming[df_all_streaming.id.str.startswith('n')]
    new_df = new_df[(new_df['release_year'] == year) & (new_df['duration_type'] == duration_type) & (new_df['type'] == 'movie')]
    new_df = new_df.sort_values(by='duration_int', ascending=False)
    new_df = new_df.reset_index(drop=True)
    resp_title = new_df['title'][0]
    resp_duration_int = new_df['duration_int'][0]
    resp_duration_type = new_df['duration_type'][0]
    return resp_title, resp_duration_int, resp_duration_type


# 5. Calcular la cantidad de Series y Películas por rating
@app.get('/5- get_rating_count')
async def get_rating_count (rating_:str):
    cantidad = len(df_all_streaming[df_all_streaming['rating'] == rating_])
    return rating_, cantidad