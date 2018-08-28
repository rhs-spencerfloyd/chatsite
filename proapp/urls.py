from django.urls import path, include

from . import views

app_name = "proapp"
urlpatterns = [
    path('', views.index, name="index"),
    path('submit', views.submit, name="submit"),
    path('setname', views.setname, name="setname"),
    path('getmessages', views.getmessages, name="getmessages"),
]
