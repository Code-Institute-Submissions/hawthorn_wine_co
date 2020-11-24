from django.urls import path
from . import views

urlpatterns = [
    path('', views.wineclub, name='wineclub'),
]
