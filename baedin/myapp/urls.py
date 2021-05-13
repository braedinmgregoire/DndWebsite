from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.home),
    path('login/', auth_views.LoginView.as_view()),
    path('register/', views.register_view),
    path('logout/', views.logout_view),
    path('characters/', views.characters_view),
    path('character/', views.character_view),
    path('index/', views.index),
    path('functions/', views.functions_view),
    path('about/', views.about),
    path('functionz/', views.functionz_view),
    path('tavern/', views.tavern, name='tavern'),
    path('tavern/<str:room_name>/', views.room, name='room')
]
