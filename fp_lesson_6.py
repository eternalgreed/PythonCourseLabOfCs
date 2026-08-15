from pymonad.state import State
from pymonad.tools import curry


@curry(3)
def walk(place, steps, visited_places):
    def count_steps(total_steps):
        new_places = visited_places + [place]
        new_total = total_steps + steps
        return new_places, new_total

    return State(count_steps)


def create_route():
    return (
        State.insert([])
        .then(walk("Дом", 0))
        .then(walk("Парк", 2000))
        .then(walk("Магазин", 1500))
    )


def main():
    visited_places, total_steps = create_route().run(0)

    print("Маршрут: " + " -> ".join(visited_places))
    print("Всего шагов: " + str(total_steps))


if __name__ == "__main__":
    main()
