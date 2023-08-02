from django.shortcuts import render
from .get_films import get_movies_by_name


def main_page(request):

    movies = get_movies_by_name('Терминатор')

    poster = movies[0]['backdrop']
    return render(request, 'main_page.html', context={'poster': poster})
