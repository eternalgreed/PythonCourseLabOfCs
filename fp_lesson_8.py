from functools import reduce


def update_maximums(maximums, number):
    largest, second_largest = maximums

    if number >= largest:
        return number, largest

    if number > second_largest:
        return largest, number

    return maximums


def second_max(numbers):
    if len(numbers) < 2:
        raise ValueError(
            "Для поиска второго максимума нужны минимум два числа"
        )

    first, second = numbers[0], numbers[1]
    initial = (first, second) if first >= second else (second, first)
    _, second_largest = reduce(update_maximums, numbers[2:], initial)
    return second_largest


def main():
    numbers = [5, 4, 3, 2, 5]
    print("Второе максимальное число: " + str(second_max(numbers)))


if __name__ == "__main__":
    main()
