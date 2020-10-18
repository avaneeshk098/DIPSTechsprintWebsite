from django.urls import path
from commerce import views
from .views import item_list

app_name = 'commerce'
urlpatterns = [
    path('home',item_list,name='item_list'),
    path('homemail', views.homemail),
    path('submail', views.submail),
    path('hints', views.hints),
    path('challenge', views.challenge),
    path('acknowledgement', views.acknowledge),
    path('scoreboard', views.scoreboard),
    path('hints/<int:id>', views.hints_post),
    path('TechSprint', views.TechSprint),
]
