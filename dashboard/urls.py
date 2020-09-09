from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path("",views.index,name="dashboard" ),
    path("add_skill",views.add_skills,name="add_skills"),
    path("placements",views.placements,name="placements"),
    path("internships",views.internships,name="internship"),
    path("offers",views.offers,name="offers")
    

]
