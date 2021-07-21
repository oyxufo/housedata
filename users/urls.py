from django.contrib import admin
from django.urls import path
import users.views

urlpatterns = [
    path('login/',users.views.login),
    path('logout/',users.views.logout),
    path('register/',users.views.register),
    path('setinfo/',users.views.setinfo),
]