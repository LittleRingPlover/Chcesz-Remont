from django.urls import path
from . import views
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticSitemap

app_name = 'remonty'

sitemaps = {
    'static': StaticSitemap
}

urlpatterns = [
    path('', views.index, name='index'),
    path('uslugi/', views.services, name='services'),
    path('o-mnie/', views.about_me, name='about_me'),
    path('galeria/', views.gallery, name='gallery'),
    path('kontakt/', views.contact, name='contact'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]