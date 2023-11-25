from django.urls import path
from . import views

urlpatterns = [
    path('playstation/', views.playstation, name="playstation"),
    path('xbox/', views.xbox, name="xbox"),
    path('nintendo/', views.nintendo, name="nintendo"),
]
