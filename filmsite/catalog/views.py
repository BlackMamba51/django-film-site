from django.shortcuts import render
from .get_films import get_movies_id, get_movies_by_id


def main_page(request):
    movies = get_movies_id('Терминатор')
    movie_id = movies[0]['id']
    movie_info = get_movies_by_id(movie_id)
    trailer_link = movie_info['videos']['trailers'][0]['url']
    persons_list = movie_info['persons']
    actors = []
    director = ''
    for person in persons_list:
        if person['enProfession'] == 'actor':
            actors.append(person['name'])
        if person['enProfession'] == 'director':
            director = person['name']
    name = movies[0]['name']
    description = movies[0]['shortDescription']
    poster = movies[0]['backdrop']
    logo = movies[0]['logo']
    return render(request, 'main_page.html', context={'name': name, 'poster': poster, 'movies': movies,
                                                      'description': description, 'logo': logo,
                                                      'trailer_link': trailer_link, 'actors': actors[:4],
                                                      'director': director})


def movies_list(request):
    movies = ['Зеленая миля', 'Побег из Шоушенка', 'Форрест Гамп', 'Список Шиндлера', '1 + 1', 'Тайна Коко',
              'Властелин колец: Возвращение короля', 'Интерстеллар', 'Бойцовский клуб', 'Унесенные призраками']
    posters = []
    # rating = movies[0]['rating']
    # alt_name = movies[0]['alternativeName']
    # year = movies[0]['year']
    # genres = movies[0]['genres'][0]
    # movie_length = movies[0]['movieLength']
    # country = movies[0]['countries'][0]
    for film in movies:
        info = get_movies_by_id(film)
        posters.append(info[0]['poster'])
    return render(request, 'catalog/movies_list.html', context={'posters': posters, 'title': movies, })
