from django.urls import path
from commerce import views
from .views import index
from django.views.generic import RedirectView
from django.contrib.sitemaps.views import sitemap
from .sitemap import StaticViewSitemap

app_name = 'commerce'
sitemaps = { 'sites': StaticViewSitemap }
urlpatterns = [
    path('',index,name='index'),
    path('homemail', views.homemail),
    path('submail', views.submail),
    path('techsprint/fps', views.gaming, name='gaming'),
    path('techsprint/thinkathon', views.thinkathon, name='thinkathon'),
    path('techsprint/decoding', views.decoding, name='decoding'),
    path('techsprint/team', views.team, name='team'),
    path('techsprint/decoding_challenge/home', views.decoding_index),
    path('techsprint/decoding_challenge/hints', views.hints),
    path('techsprint/decoding_challenge/challenge', views.challenge),
    path('techsprint/decoding_challenge/acknowledgement', views.acknowledge),
    path('techsprint/decoding_challenge/scoreboard', views.scoreboard),
    path('techsprint/decoding_challenge/hints/<int:id>', views.hints_post),
    path('techsprint', views.techsprint, name='techsprint'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps },name='django.contrib.sitemaps.views.sitemap'),
]
