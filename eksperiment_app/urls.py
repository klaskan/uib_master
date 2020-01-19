from django.urls import path
from eksperiment_app import views as eksperiment_views
from . import views

urlpatterns = [
    path('', eksperiment_views.index, name='index'),
    path('about/', views.about, name='about'),
    path('eksperiment/', views.eksperiment, name='eksperiment'),
    path('waiting/', views.waiting, name='waiting'),
    path('revidert/', views.revidert, name='revidert'),
    
]
