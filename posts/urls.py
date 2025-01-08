#python
# posts/urls.py

from django.urls import path
from .views import list_posts

urlpatterns = [
    path('', list_posts, name='list_posts'),
]