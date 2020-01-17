from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('gdz/', views.main_page, name="main-page"),
    path('nom_detail/<int:number_of_task>/', views.nom_detail, name='main-detail'),
]