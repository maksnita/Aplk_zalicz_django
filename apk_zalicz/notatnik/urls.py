from django.urls import path
from . import views

urlpatterns = [
    path('', views.notatnik, name="notatnik"),
    path('baza/', views.baza, name="baza")
]