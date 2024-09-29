from django.contrib import admin
from .models import Profile, Movie, Rating

class MovieAdmin(admin.ModelAdmin):
    search_fields = ['title']

class RatingAdmin(admin.ModelAdmin):
    list_display = ['user', 'movie', 'rating']

# Register your models here.
admin.site.register(Profile)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Rating, RatingAdmin)