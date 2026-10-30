from django.urls import path
from . import views

urlpatterns = [
    path('', views.careers_view, name='careers'),
]