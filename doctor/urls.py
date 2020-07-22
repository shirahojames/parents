from django.urls import path
from . import views
urlpatterns = [
        path('', views.home, name='home'),
        path('login/', views.logindoctor, name='logindoctor'),
        path('signup/', views.signupdoctor, name='signupdoctor'),
]
