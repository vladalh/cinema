import json
import random
import csv


def making_films():
    """
    Creating movie dictionaries
    """
    name_cinema_list_1 = ["I", "all", "we", "always", "yesterday", "sailing", "go", "house",
                          "stadium", "clouds", "window", "locked", "a door", "close", "television"]
    name_cinema_list_2 = ["airplane", "fly", "run away", "dog", "cat", "arrow", "siren", "moon",
                          "sun", "ship", "a boat", "war", "peace", "bird", "ball"]
    name_cinema_list_3 = ["about", "talk", "wedding", "scenario", "dumb", "disabled person", "he",
                          "you", "young woman", "boy", "father", "nanny", "think", "only", "kiss"]

    genres_cinema = ["horrors", "fantastic", "thriller", "melodrama", "military", "about love",
                     "comedy", "detective", "erotica", "historical", "cartoon", "western film", "anime"]

    country_of_origin = ["USA", "Canada", "France", "Russia", "Italy", "United Kingdom", "Poland",
                         "Germany", "China", "Korea", "Turkey", "Brasil", "Belarus", "Mexico", "Romania"]

    a = 1
    cinema_full_dict = {}
    cinema_dict = {}
    cinema_list = []
    genres_set = set()
    country_set = set()

    while a <= 20:
        num = random.randint(1, 1000000)
        cinema_list.append(num)
        if cinema_list.count(num) >= 2:
            num = random.randint(1, 1000000)
            cinema_list.append(num)
        for num in cinema_list:
            movie_number = num
        cinema_list.clear()

        full_name = (str(random.choice(name_cinema_list_1)) + " " + str(random.choice(name_cinema_list_2)) +
                     " " + str(random.choice(name_cinema_list_3)))

        rating = sum([random.randint(1, 100) for k in range(100)]) / 100

        production_year = random.randint(1895, 2021)

        genre_count = random.randint(1, 3)
        for i in range(genre_count):
            genre = random.choice(genres_cinema)
            cinema_list.append(genre)
            genres_set = set(cinema_list)
            if len(genres_set) < genre_count:
                cinema_list.append(random.choice(genres_cinema))
                genres_set = set(cinema_list)
            cinema_list.clear()

        country_count = random.randint(1, 3)
        for j in range(country_count):
            country = random.choice(country_of_origin)
            country_set.add(country)
            if len(country_set) < country_count:
                country_set.add(random.choice(country_of_origin))

        cinema_dict = {
            "movie number": movie_number,
            "movie title": full_name,
            "mark": rating,
            "year of issue": production_year,
            "genre": list(genres_set),
            "country": tuple(random.sample(country_of_origin, country_count))}
        a += 1

        cinema_full_dict[movie_number] = cinema_dict
    return cinema_full_dict


def file_write(fileformat, cinema_full_dict):
    """
    Writing movie dictionaries to file formats txt, csv, json
    """
    with open(f"movies.{fileformat}", "w", encoding="utf-8") as file:
        if fileformat == "txt":
            for key, value in cinema_full_dict.items():
                txt_file = file.write(f"{key}: {value}\n")

        elif fileformat == "csv":
            columns = ["movie number", "movie title", "mark", "year of issue", "genre", "country"]
            csv_file = csv.DictWriter(file, fieldnames=columns)
            csv_file.writeheader()
            csv_file.writerows(cinema_full_dict.values())

        elif fileformat == "json":
            json_file = json.dump(cinema_full_dict, file, indent=4)


def file_reader(fileformat):
    """
    Reading previously recorded movie dictionary files
    """
    cinema_list = []
    with open(f"movies.{fileformat}", "r", encoding="utf-8") as file:
        if fileformat == "txt":
            for line in file:
                file_list = line.split(",")
                cinema_list.append(file_list)

        elif fileformat == "csv":
            csv_reader = csv.DictReader(file, delimiter=",")
            for line in csv_reader:
                if any(line):
                    cinema_list.append(line)

        elif fileformat == 'json':
            cinema_list = json.load(file)
    return cinema_list


def file_processing(fileformat, cinema_list, person):
    """
    Processing read files
    """
    criterion_list = []
    if fileformat == "txt":
        for cinema in cinema_list:
            if person.isdigit():
                if int(person) > 1895:
                    cin1 = cinema[3].strip().split(":")
                    cin2 = cin1[1]
                    if int(person) <= int(cin2):
                        criterion_list.append(cinema)

                elif int(person) < 100:
                    cin3 = cinema[2].strip().split(":")
                    cin4 = cin3[1]
                    if int(person) <= float(cin4):
                        criterion_list.append(cinema)

            elif person.isalpha():
                if person in cinema[4]:
                    criterion_list.append(cinema)

                elif person in cinema[5]:
                    criterion_list.append(cinema)

    elif fileformat == "csv":
        for cinema in cinema_list:
            if person.isdigit():
                if int(person) >= 1895 and int(person) <= int(cinema["year of issue"]):
                    criterion_list.append(cinema)
                elif int(person) <= 100 and int(person) <= float(cinema["mark"]):
                    criterion_list.append(cinema)
            elif person.isalpha():
                if person in cinema["genre"]:
                    criterion_list.append(cinema)
                elif person in cinema["country"]:
                    criterion_list.append(cinema)

    elif fileformat == "json":
        for cin in cinema_list:
            if person.isdigit():
                if int(person) >= 1895 and int(person) <= cinema_list[cin]["year of issue"]:
                    criterion_list.append(cinema_list[cin])
                elif int(person) <= 100 and int(person) <= float(cinema_list[cin]["mark"]):
                    criterion_list.append(cinema_list[cin])
            elif person.isalpha():
                if person in cinema_list[cin]["genre"]:
                    criterion_list.append(cinema_list[cin])
                elif person in cinema_list[cin]["country"]:
                    criterion_list.append(cinema_list[cin])
    return criterion_list


def criterion_write(fileformat, criterion_list):
    """
    Recording files according to selected criteria
    """
    result_mmovies = ""
    for res in criterion_list:
        result = ",".join(res)
        result_mmovies += result
    with open(f"result_mmovies.{fileformat}", "w", encoding="utf-8") as file:
        if fileformat == "txt":
            file.write(result_mmovies)

        elif fileformat == "csv":
            columns = ["movie number", "movie title", "mark", "year of issue", "genre", "country"]
            csv_file = csv.DictWriter(file, fieldnames=columns)
            csv_file.writeheader()
            csv_file.writerows(criterion_list)

        elif fileformat == "json":
            json_file = json.dump(criterion_list, file, indent=4)

# vladalh@mail.ru
