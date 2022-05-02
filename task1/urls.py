from django.urls import path, include
from .views import index, post_ok

urlpatterns = [
   path('', index, name='index'),
   path('/post_ok', post_ok, name='post_ok'),
]
