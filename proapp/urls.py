from django.urls import path, include

from . import views

app_name = "proapp"
urlpatterns = [
    path('', views.index, name="index"),
    path('submit', views.submit, name="submit"),
    path('results', views.results, name="results"),
    path('getmessages', views.getmessages, name="getmessages"),
]
