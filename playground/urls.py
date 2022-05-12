from django.urls import path
from . import views

urlpatterns = [
    path('hello/<str:startYear>/<str:endYear>/<str:region>', views.say_hello)
]
