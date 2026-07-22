# -*- coding: utf-8 -*-


def read_age():
    while True:
        answer = input("Введите ваш возраст: ")

        try:
            age = int(answer)
        except ValueError:
            print("Ошибка: возраст нужно ввести целым числом.")
            continue

        if age < 0:
            print("Ошибка: возраст не может быть отрицательным.")
            continue

        return age


def create_summary(name, city, age):
    return [
        "Здравствуйте, " + name + "!",
        "Ваш город: " + city,
        "Ваш возраст: " + str(age),
        "Через год ваш возраст будет: " + str(age + 1),
    ]


def main():
    print("Проверка консольного ввода в Python")

    name = input("Введите ваше имя: ").strip()
    city = input("Введите ваш город: ").strip()
    age = read_age()

    print()

    for line in create_summary(name, city, age):
        print(line)


if __name__ == "__main__":
    main()
