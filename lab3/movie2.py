from movie import movies, is_high_rated, high_rated_movies, movies_by_category, average_imdb, average_imdb_by_category

print("Is 'Hitman' high rated?", is_high_rated(movies[1]))
print("\nMovies with high rating:", high_rated_movies(movies))
print("\nAction movies:", movies_by_category(movies, "Action"))
print("\nAverage IMDB of all movies:", average_imdb(movies))
print("\nAverage IMDB of Romance movies:", average_imdb_by_category(movies, "Romance"))