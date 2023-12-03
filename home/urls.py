from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path(
        'confirm_delete_account/',
        views.confirm_delete_account,
        name='confirm_delete_account'),
]
