from django.urls import path
from . import views

app_name = "website"

urlpatterns = [
    path('home', views.home_page_view, name='home'),
    path('about', views.about_page_view, name='about'),
    path('index', views.index_page_view, name='index'),
]