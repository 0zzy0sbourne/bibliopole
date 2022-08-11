from django.urls import path
from . import views 

urlpatterns = [
    # /films/
    path('', views.index, name="index"), 
    # /films/5/
    path('<slug:film_title>/', views.detail, name='detail'),
    # /films/5/results/
    path('<slug:film_title>/results', views.results, name='results'), 
    # /films/5/vote/
    path('<slug:film_title>/vote/', views.vote, name='vote')
]