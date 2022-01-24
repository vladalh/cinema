import csv
import json
from cinema2 import Cinema_dict


class Working_file():
    pass
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
            json_file = json.dump(cinema_full_dict(), file, indent=4)


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

