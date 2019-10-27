from django.conf.urls import url
from django.contrib import admin
from  . import views
urlpatterns = [
    # url(r'^', views.home),
    url(r'^home', views.home, name='home'),
    url(r'^abb_book', views.add_book, name='add_book'),
    url(r'^add/$', views.add, name='add'),
    url(r'^add/succeed', views.succeed, name='succeed')
]