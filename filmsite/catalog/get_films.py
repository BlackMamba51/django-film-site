import requests

headers = {'X-API-KEY': 'Y26BHV6-VK7M9EZ-KP1PBSY-41NJPNE'}


def get_movies_id(name, page=1, limit=1):
    response = requests.get(
        'https://api.kinopoisk.dev/v1.2/movie/search',
        params={
            "query": name,
            "limit": limit,
            "page": page,
        },
        headers=headers
    )
    movies = response.json()
    return movies['docs']


def get_movies_by_id(movie_id):
    response = requests.get(
        f'https://api.kinopoisk.dev/v1.3/movie/{movie_id}',
        params={
            'id': movie_id,
        },
        headers=headers
    )
    movie = response.json()
    return movie



