from cinema import Cinema
import random


class Cinema_dict():
    #pass
    def create_cinema_dict(self):
        a = 1
        cinema_full_dict = {}
        cinema_dict = {}
        cinema_list = []
        while a <= 20:
            num = random.randint(1, 1000000)
            cinema_list.append(num)
            if cinema_list.count(num) >= 2:
                num = random.randint(1, 1000000)
                cinema_list.append(num)
            for num in cinema_list:
                movie_number = num
            cinema_list.clear()

            movie = Cinema()
            cinema_dict = {
                "movie number": movie_number,
                "movie title": movie.create_name_movie(),
                "mark": movie.create_rating(),
                "year of issue": movie.create_prodaction_year(),
                "genre": movie.create_genre_movie(),
                "country": movie.create_country_movie()}
            a += 1
            cinema_full_dict[movie_number] = cinema_dict
        return cinema_full_dict

