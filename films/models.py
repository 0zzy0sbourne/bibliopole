from django.db import models

class Film(models.Model): 
    def __str__(self): 
        return self.film_title
    def as_dict(self): 
        return {
            "film_title": self.film_title, 
            "film_director": self.film_director, 
            "film_rating": "self.film_rating"
        }
    film_title=models.CharField(max_length=200)
    film_director=models.CharField(max_length=200)
    film_rating=models.FloatField()