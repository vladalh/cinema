from cinema3 import Working_file
from cinema2 import Cinema_dict


def main():
    file_format_list = ["txt", "csv", "json"]

    file_format = input("Enter the file format for saving data: txt, csv or json: ")

    dict_save_path = input("Enter the path to save the movie dictionary: (optional step, you can click 'enter') ")

    if file_format not in file_format_list:
        print("You entered the wrong file format")
        exit(0)

    person = input("Enter year, rating, country or genre:")

    result_path = input(
        "Enter the path to save the list by selection criterion: (optional step, you can click 'enter')")

    Working_file().file_write(file_format, Cinema_dict().create_cinema_dict())
    Working_file().criterion_write(file_format, Working_file().file_processing(file_format,
                                            Working_file().file_reader(file_format), person))


if __name__ == "__main__":
    main()
