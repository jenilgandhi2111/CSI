from django.contrib import admin
from django.urls import path,include
from . import views
from dashboard import views as dashboard_view
urlpatterns = [
    path('',views.index,name="login_home"),
   
   
]
