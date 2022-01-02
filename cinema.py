import random


def cinema_full_name(list1, list2, list3):
    full_name = (str(random.choice(list1)) + " " + str(random.choice(list2)) +
                 " " + str(random.choice(list3)))
    return full_name


def cinema_id_number():
    cinema_list = []
    num = random.randint(1, 1000000)
    cinema_list.append(num)
    if cinema_list.count(num) >= 2:
        num = random.randint(1, 1000000)
        cinema_list.append(num)
    for num in cinema_list:
        movie_number = num
    return movie_number



def genres_cinema(genres_cinema_list):
    cinema_list = []
    genre_count = random.randint(1, 3)
    for i in range(genre_count + 1):
        genre = random.choice(genres_cinema_list)
        cinema_list.append(genre)
        genres_set = set(cinema_list)
        if len(genres_set) < genre_count:
            cinema_list.append(random.choice(genres_cinema_list))
            genres_set = set(cinema_list)
    return genres_set


def cinema_rating():
    rating = sum([random.randint(1, 100) for i in range(100)]) / 100
    return rating


def country_of_origin(list1):
    country_set = set()
    country_count = random.randint(1, 3)
    for i in range(country_count):
        country = random.choice(list1)
        country_set.add(country)
        if len(country_set) < country_count:
            country_set.add(random.choice(list1))
    return country_set


name_cinema_list_1 = ["I", "all", "we", "always", "yesterday", "sailing", "go", "house",
                      "stadium", "clouds", "window", "locked", "a door", "close", "television"]
name_cinema_list_2 = ["airplane", "fly", "run away", "dog", "cat", "arrow", "siren", "moon",
                      "sun", "ship", "a boat", "war", "peace", "bird", "ball"]
name_cinema_list_3 = ["about", "talk", "wedding", "scenario", "dumb", "disabled person", "he",
                      "you", "young woman", "boy", "father", "nanny", "think", "only", "kiss"]

genres_cinema_list = ["horrors", "fantastic", "thriller", "melodrama", "military", "about love",
                 "comedy", "detective", "erotica", "historical", "cartoon", "western film", "anime"]

country_of_origin_list = ["USA", "Canada", "France", "Russia", "Italy", "United Kingdom", "Poland",
                     "Germany", "China", "Korea", "Turkey", "Brasil", "Belarus", "Mexico", "Romania"]

a = 1
cinema_full_dict = {}
cinema_dict = {}
cinema_list = []

while a <= 20:
    production_year = random.randint(1895, 2021)

    cinema_dict = {
        "movie number": cinema_id_number(),
        "movie title": cinema_full_name(name_cinema_list_1, name_cinema_list_2, name_cinema_list_3),
        "mark": cinema_rating(),
        "year of issue": production_year,
        "genre": genres_cinema(genres_cinema_list),
        "country": tuple(country_of_origin(country_of_origin_list))
    }
    a += 1

    print(cinema_dict)
    cinema_full_dict[cinema_id_number()] = cinema_dict
print(cinema_full_dict)

person = input("Enter year, rating, country or genre:")
msg = ""

for k in cinema_full_dict:
    if person.isdigit():
        if int(person) <= cinema_full_dict[k]["year of issue"]:
            cinema_list.append(cinema_full_dict[k])
            msg = f"list of films for a given request :{cinema_list}"

        elif float(person) < float(cinema_full_dict[k]["mark"]):
            cinema_list.append(cinema_full_dict[k])
            msg = f"list of films for a given request :{cinema_list}"

        else:
            msg = f"There are no films with such parameters"

    elif person.isalpha():
        for l in cinema_full_dict[k]["genre"]:
            if person == l:
                cinema_list.append(cinema_full_dict[k])
                msg = f"list of films for a given request :{cinema_list}"

            if person in cinema_full_dict[k]["country"]:
                cinema_list.append(cinema_full_dict[k])
                msg = f"list of films for a given request :{cinema_list}"

    else:
        msg = f"The input format does not meet the requirement. Restart the program and re-enter"

print(msg)

# vladalh@mail.ru
