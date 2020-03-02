# @author Simranjit Singh
from django.urls import path

from store import views

urlpatterns = [
    path('', views.store, name='store'),
    path('index', views.index, name='index')
    ]