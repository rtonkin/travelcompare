from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('travelsites/<product>/<sitea>-vs-<siteb>/', views.sitecomparison, name='comparison'),
    path('travelsites/features/<slug>/', views.featurecomparison, name='feature'),
    path('travelsites/<product>/<slug>/', views.site, name='site'),
    path('articles/all/', views.allarticles, name='allarticles'),
    path('articles/<slug>/', views.article, name='article'),
    path('about/', views.about, name='about'),
    path('mainpage-autocomplete/', views.MainPageAutocomplete.as_view(), name='mainpage-autocomplete'),
]
