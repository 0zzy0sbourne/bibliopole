from curses.ascii import HT
from django.shortcuts import render
from django.http import HttpResponse

def index(request): 
    return HttpResponse("Hello world, you're in the bibliopole")
def detail(request, film_title): 
    return HttpResponse("You're looking at film " + film_title)
def results(request, film_title): 
    response = "Your're looking at the results of question %s."
    return HttpResponse(response + film_title)
def vote(request, film_title): 
    return HttpResponse("You're voting on film " + film_title)
