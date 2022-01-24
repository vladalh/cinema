import random


class Cinema():
    def create_name_movie(self):
        """
        Creating name movie
        """
        name_cinema_list_1 = ["I", "all", "we", "always", "yesterday", "sailing", "go", "house",
                          "stadium", "clouds", "window", "locked", "a door", "close", "television"]
        name_cinema_list_2 = ["airplane", "fly", "run away", "dog", "cat", "arrow", "siren", "moon",
                          "sun", "ship", "a boat", "war", "peace", "bird", "ball"]
        name_cinema_list_3 = ["about", "talk", "wedding", "scenario", "dumb", "disabled person", "he",
                          "you", "young woman", "boy", "father", "nanny", "think", "only", "kiss"]
        full_name = (str(random.choice(name_cinema_list_1)) + " " + str(random.choice(name_cinema_list_2)) +
                     " " + str(random.choice(name_cinema_list_3)))
        return full_name


    def create_rating(self):
        rating = sum([random.randint(1, 100) for k in range(100)]) / 100
        return rating


    def create_prodaction_year(self):
        production_year = random.randint(1895, 2021)
        return production_year


    def create_genre_movie(self):
        genres_cinema = ["horrors", "fantastic", "thriller", "melodrama", "military", "about love",
                     "comedy", "detective", "erotica", "historical", "cartoon", "western film", "anime"]
        genre_count = random.randint(1, 3)
        cinema_list = []
        for i in range(genre_count):
            genre = random.choice(genres_cinema)
            cinema_list.append(genre)
            genres_set = set(cinema_list)
            if len(genres_set) < genre_count:
                cinema_list.append(random.choice(genres_cinema))
                genres_set = set(cinema_list)
            cinema_list.clear()
            genres= list(genres_set)
        return genres


    def create_country_movie(self):
         country_of_origin = ["USA", "Canada", "France", "Russia", "Italy", "United Kingdom",
                              "Poland", "Germany", "China", "Korea", "Turkey", "Brasil",
                              "Belarus", "Mexico", "Romania", "Japan"]
         country_count = random.randint(1, 3)
         countries = tuple(random.sample(country_of_origin, country_count))
         return countries

# vladalh@mail.ru
