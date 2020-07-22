from django.urls import path
from . import views
urlpatterns = [
        path('', views.homepage, name='homepage'),
        path('login/', views.loginparent, name='loginparent'),
        path('signup/', views.signupparent, name='signupparent'),
]
