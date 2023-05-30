from django.urls import path

from . import views
from .views import *

app_name = 'blog'

urlpatterns = [
    path('title', blog_title, name='blog_title'),
    path('<int:article_id>',blog_article,name='blog_article')
]