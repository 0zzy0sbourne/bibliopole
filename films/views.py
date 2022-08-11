from curses.ascii import HT
import json
from unittest import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from films.models import Film
from django.shortcuts import render
from django.forms.models import model_to_dict

query = {
    "bool": {
        "must": []
    } 
}

def index(request): 
    film_list = Film.objects.all()
    dictionaries = [ obj.as_dict() for obj in film_list ]
    return HttpResponse(json.dumps({"data": dictionaries}), content_type='application/json')

    #template = loader.get_template('films/index.html')
    #context = {'film_list' : film_list}
    #response_data = {}
    #response_data["first_film"] = film_list[0]
    #response_data["second_film"] = film_list[1]
    #return render(request, 'films/index.html', context)    
    #return HttpResponse(json.dumps(film_list), content_type="application/json")

def detail(request, film_title): 
    return HttpResponse("You're looking at film " + film_title)
def results(request, film_title): 
    response = "Your're looking at the results of question "
    return HttpResponse(response + film_title)
def vote(request, film_title): 
    return HttpResponse("You're voting on film " + film_title)
