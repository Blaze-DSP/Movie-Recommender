from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path("", views.Home, name='Home'),
    path("Genres", views.Genres, name='Genres'),
    path("Register", views.Register, name='Register'),
    path("Login", views.Login, name='Login'),
    path("Form", views.Form, name='Form'),
    path("Movies/<str:title>", views.Details , name='Movies'),
    path("Movies/<str:title>/Similar", views.Similar, name='Similar'),
    path("Logout", views.Logout, name='Logout'),
]