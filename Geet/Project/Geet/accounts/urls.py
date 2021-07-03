from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    url('register/', views.registration, name="signup"),
    url('login/', views.loginUser, name="login"),
    url('logout/', views.logoutUser, name="logout"),
    url('upload/', views.upload, name="upload"),
    url('startlistening/player/<int:id>/', views.player, name="player"),
    url('startlistening/', views.startlistening, name="startlistening"),
    url('channel/',views.channel,name="channel"),
    url('', views.index, name="home"),
    
]

