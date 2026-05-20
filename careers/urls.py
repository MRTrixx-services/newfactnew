from django.urls import path
from . import views

urlpatterns = [
    path('careers/', views.careers_view, name='careers'),
]