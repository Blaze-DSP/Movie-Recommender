from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import pandas as pd
import joblib
import keras
import tensorflow as tf

@keras.saving.register_keras_serializable()
class L2NormalizationLayer(keras.layers.Layer):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def call(self, inputs):
        return tf.linalg.l2_normalize(inputs, axis=1)
    
    def get_config(self):
        return super().get_config()
    
    
model_m = keras.saving.load_model('./utils/models/movie.keras')
model_u = keras.saving.load_model('./utils/models/user.keras')

scale_movie = joblib.load("./utils/scalers/scale_movie.pkl")
scale_user = joblib.load("./utils/scalers/scale_user.pkl")
scale_target = joblib.load("./utils/scalers/scale_target.pkl")

movie_out = pd.read_parquet('./utils/data/movie_out.parquet')
movie_info = pd.read_parquet("./utils/data/movie_info.parquet")

def dist(a,b):
    return (np.linalg.norm(a-b))**2

app = FastAPI()

class genre_input(BaseModel):
    input: list
    title: str
class genre_output(BaseModel):
    movies: list
@app.post('/genres/predict')
def func(input_param: genre_input):
    title = input_param.title
    movie_feat = np.array([input_param.input])
    movie_feat = scale_movie.transform(movie_feat)
    output = model_m.predict([movie_feat])

    similar = np.array([[0,0]])
    for i in range(1000):
        differences = dist(output[0], movie_out.to_numpy()[i,1:])
        record = np.array([movie_out.to_numpy()[i,0], differences])
        similar = np.vstack((similar, record))

    similar = similar[1:,:]
    similar = similar[np.argsort(similar[:, 1])]

    movies = []
    i=0
    while i<10:
        tmp = movie_info[movie_info['id'] == int(similar[i,0])]
        if (title != tmp['title'].iloc[0]):
            movies.append(tmp['title'].iloc[0])
            i+=1
    
    response = genre_output(movies=movies)
    return response



class user_input(BaseModel):
    input: list
class user_output(BaseModel):
    movies: list
@app.post('/user/predict')
def func(input_param: user_input):
    user_feat = np.array([input_param.input])
    user_feat = scale_user.transform(user_feat)
    user_out = model_u.predict(user_feat)    
    movies = movie_out.to_numpy()[:,1:]

    predictions = np.matmul(movies,user_out.T)
    predictions = scale_target.inverse_transform(predictions)
    idx  = np.argsort(-predictions[:,0])
    similar = movie_info.to_numpy()[idx]
        
    movies = []
    for i in range(10):
        movies.append(similar[i][1])
    
    response = user_output(movies=movies)
    return response


