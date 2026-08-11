from pymonad.maybe import Just, Nothing
from pymonad.tools import curry


@curry(2)
def to_left(number, pole):
    left, right = pole
    new_pole = [left + number, right]

    if abs(new_pole[0] - new_pole[1]) > 4:
        return Nothing

    return Just(new_pole)


@curry(2)
def to_right(number, pole):
    left, right = pole
    new_pole = [left, right + number]

    if abs(new_pole[0] - new_pole[1]) > 4:
        return Nothing

    return Just(new_pole)


def banana(pole):
    return Nothing


def begin():
    return Just([0, 0])


def show(maybe):
    if maybe == Nothing:
        print(False)
    else:
        print(f"True: {maybe.value}")


def main():
    show(
        begin()
        .bind(to_left(2))
        .bind(to_right(5))
        .bind(to_left(-2))
    )
    show(
        begin()
        .bind(to_left(2))
        .bind(to_right(5))
        .bind(to_left(-1))
    )
    show(
        begin()
        .bind(to_left(2))
        .bind(banana)
        .bind(to_right(5))
        .bind(to_left(-1))
    )


if __name__ == "__main__":
    main()
