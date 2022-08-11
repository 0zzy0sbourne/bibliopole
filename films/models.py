from django.db import models

class Film(models.Model): 
    def __str__(self): 
        return self.film_title
    film_title=models.CharField(max_length=200)
    film_director=models.CharField(max_length=200)
    film_rating=models.FloatField()