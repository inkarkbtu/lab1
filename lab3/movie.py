movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Help", "imdb": 8.0, "category": "Drama"},
    {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
    {"name": "Colonia", "imdb": 7.4, "category": "Romance"},
    {"name": "Love", "imdb": 6.0, "category": "Romance"},
    {"name": "Bride Wars", "imdb": 5.4, "category": "Romance"},
    {"name": "AlphaJet", "imdb": 3.2, "category": "War"},
    {"name": "Ringing Crime", "imdb": 4.0, "category": "Crime"},
    {"name": "Joking muck", "imdb": 7.2, "category": "Comedy"},
    {"name": "What is the name", "imdb": 9.2, "category": "Suspense"},
    {"name": "Detective", "imdb": 7.0, "category": "Suspense"},
    {"name": "Exam", "imdb": 4.2, "category": "Thriller"},
    {"name": "We Two", "imdb": 7.2, "category": "Romance"}
]

#Проверка, имеет ли фильм рейтинг выше 5.5
def is_high_rated(movie):
    return movie["imdb"] > 5.5

#Возвращает список фильмов с рейтингом выше 5.5
def high_rated_movies(movie_list):
    return [movie for movie in movie_list if movie["imdb"] > 5.5]

#Возвращает список фильмов по категории
def movies_by_category(movie_list, category):
    return [movie for movie in movie_list if movie["category"] == category]

#Вычисляет средний рейтинг списка фильмов
def average_imdb(movie_list):
    if not movie_list:
        return 0
    return sum(movie["imdb"] for movie in movie_list) / len(movie_list)

#Вычисляет средний рейтинг фильмов в указанной категории
def average_imdb_by_category(movie_list, category):
    category_movies = movies_by_category(movie_list, category)
    return average_imdb(category_movies)