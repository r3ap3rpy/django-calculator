from django.urls import path
from . import views

urlpatterns = [
    path('multiply/',views.index, name = 'multiply'),
]