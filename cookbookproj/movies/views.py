from django.shortcuts import render
from .models import Category


def movie_category_list(request):
    context = {
        'categories': Category.objects.all(),
    }
    return render(
        request,
        'movies/movie_category_list.html',
        context,
    )
