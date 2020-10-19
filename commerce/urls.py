from django.urls import path
from commerce import views
from .views import item_list
from django.views.generic import RedirectView
app_name = 'commerce'
urlpatterns = [
    path('',item_list,name='item_list'),
    path('homemail', views.homemail),
    path('submail', views.submail),
    path('techsprint/fps', views.gaming),
    path('techsprint/thinkathon', views.thinkathon),
    path('techsprint/decoding', views.decoding),
    path('techsprint/team', views.team),
    path('techsprint/decoding_challenge/home', views.index),
    path('techsprint/decoding_challenge/hints', views.hints),
    path('techsprint/decoding_challenge/challenge', views.challenge),
    path('techsprint/decoding_challenge/acknowledgement', views.acknowledge),
    path('techsprint/decoding_challenge/scoreboard', views.scoreboard),
    path('techsprint/decoding_challenge/hints/<int:id>', views.hints_post),
    path('techsprint', views.TechSprint),
]
