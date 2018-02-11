from django.urls import path

from .views import movie_category_list


urlpatterns = [
    path('', movie_category_list, name='movie_category_list'),
]
