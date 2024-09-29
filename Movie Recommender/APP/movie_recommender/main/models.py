from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='User')

    Adventure = models.CharField(max_length=100, null=False, verbose_name='Adventure')
    Animation = models.CharField(max_length=100, null=False, verbose_name='Animation')
    Children = models.CharField(max_length=100, null=False, verbose_name='Children')
    Comedy = models.CharField(max_length=100, null=False, verbose_name='Comedy')
    Fantasy = models.CharField(max_length=100, null=False, verbose_name='Fantasy')
    Romance = models.CharField(max_length=100, null=False, verbose_name='Romance')
    Drama = models.CharField(max_length=100, null=False, verbose_name='Drama')
    Action = models.CharField(max_length=100, null=False, verbose_name='Action')
    Crime = models.CharField(max_length=100, null=False, verbose_name='Crime')
    Thriller = models.CharField(max_length=100, null=False, verbose_name='Thriller')
    Horror = models.CharField(max_length=100, null=False, verbose_name='Horror')
    Mystery = models.CharField(max_length=100, null=False, verbose_name='Mystery')
    Sci_Fi = models.CharField(max_length=100, null=False, verbose_name='Sci_Fi')
    IMAX = models.CharField(max_length=100, null=False, verbose_name='IMAX')
    Documentary = models.CharField(max_length=100, null=False, verbose_name='Documentary')
    War = models.CharField(max_length=100, null=False, verbose_name='War')
    Musical = models.CharField(max_length=100, null=False, verbose_name='Musical')
    Western = models.CharField(max_length=100, null=False, verbose_name='Western')
    Film_Noir = models.CharField(max_length=100, null=False, verbose_name='Film_Noir')

    def __str__(self):
        return self.user.username

class Movie(models.Model):
    title = models.CharField(max_length=100, null=False, verbose_name='Title')

    Adventure = models.BooleanField(verbose_name='Adventure')
    Animation = models.BooleanField(verbose_name='Animation')
    Children = models.BooleanField(verbose_name='Children')
    Comedy = models.BooleanField(verbose_name='Comedy')
    Fantasy = models.BooleanField(verbose_name='Fantasy')
    Romance = models.BooleanField(verbose_name='Romance')
    Drama = models.BooleanField(verbose_name='Drama')
    Action = models.BooleanField(verbose_name='Action')
    Crime = models.BooleanField(verbose_name='Crime')
    Thriller = models.BooleanField(verbose_name='Thriller')
    Horror = models.BooleanField(verbose_name='Horror')
    Mystery = models.BooleanField(verbose_name='Mystery')
    Sci_Fi = models.BooleanField(verbose_name='Sci_Fi')
    IMAX = models.BooleanField(verbose_name='IMAX')
    Documentary = models.BooleanField(verbose_name='Documentary')
    War = models.BooleanField(verbose_name='War')
    Musical = models.BooleanField(verbose_name='Musical')
    Western = models.BooleanField(verbose_name='Western')
    Film_Noir = models.BooleanField(verbose_name='Film_Noir')

    def __str__(self):
        return self.title
    
class Rating(models.Model):
    movie = models.OneToOneField(Movie, on_delete=models.CASCADE, verbose_name="movie")
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="user")

    rating = models.FloatField(null=False, verbose_name="ratings")

    def __str__(self):
        return self.user.username + ': ' + self.movie.title
# Save Ratings?