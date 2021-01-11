from django.contrib import admin
from django.urls import include, path
from main import views
from django.contrib.sitemaps.views import sitemap
from .sitemaps import SiteProductSitemap, ArticleSitemap, qAndASitemap

sitemaps = {'siteproducts': SiteProductSitemap, 'articles': ArticleSitemap, 'qanda': qAndASitemap}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('index2/', views.index2, name='index2'),
    path('travelsites/<product>/<sitea>-vs-<siteb>/', views.sitecomparison, name='comparison'),
    path('travelsites/features/<slug>/', views.featurecomparison, name='feature'),
    path('travelsites/<product>/<slug>/', views.site, name='site'),
    path('articles/all/', views.allarticles, name='allarticles'),
    path('articles/<slug>/', views.article, name='article'),
    path('questions/tag/<slug>/', views.questionAnswerTag, name='questionstag'),
    path('questions/all/', views.questionAnswerList, name='questionslist'),
    path('questions/<slug>/', views.questionAnswer, name='questions'),
    path('recommendations/beijing/', views.rec_beijing, name='recbj'),
    path('recommendations/shanghai/', views.rec_shanghai, name='recsh'),
    path('recommendations/shenzhen/', views.rec_shenzhen, name='recsz'),
    path('recommendations/guangzhou/', views.rec_guangzhou, name='recgz'),
    path('about/', views.about, name='about'),
    path('mainpage-autocomplete/', views.MainPageAutocomplete.as_view(), name='mainpage-autocomplete'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('user', views.userPanel),
    path('ajax/get_user_info', views.getUserInfo, name='get_user_info'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
