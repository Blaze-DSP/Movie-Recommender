import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movie_recommender.settings')
django.setup()

import pandas as pd
from main.models import Movie
dataframe = pd.read_parquet("./dataset/movie_info.parquet")
for index, row in dataframe.iterrows():
    Movie.objects.create(title=row['title'],Adventure=row['Adventure'],Animation=row['Animation'],Children=row['Children'],Comedy=row['Comedy'],Fantasy=row['Fantasy'],Romance=row['Romance'],Drama=row['Drama'],Action=row['Action'],Crime=row['Crime'],Thriller=row['Thriller'],Horror=row['Horror'],Mystery=row['Mystery'],Sci_Fi=row['Sci-Fi'],IMAX=row['IMAX'],Documentary=row['Documentary'],War=row['War'],Musical=row['Musical'],Western=row['Western'],Film_Noir=row['Film-Noir'])