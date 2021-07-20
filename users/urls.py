from django.contrib import admin
from django.urls import path
import showdata.views

urlpatterns = [
    path('login/',showdata.views.login),


]