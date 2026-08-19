from functools import partial
from itertools import accumulate, chain, repeat


def get_neighbors(area):
    row, column = area
    return (
        (row - 1, column),
        (row + 1, column),
        (row, column - 1),
        (row, column + 1),
    )


def is_inside(n, m, area):
    row, column = area
    return 1 <= row <= n and 1 <= column <= m


def capture_next_day(n, m, captured):
    neighbors = chain.from_iterable(map(get_neighbors, captured))
    available_neighbors = filter(partial(is_inside, n, m), neighbors)
    return captured | set(available_neighbors)


def count_days(n, m, captured):
    next_day = partial(capture_next_day, n, m)
    campaign = accumulate(
        repeat(None),
        lambda current, _: next_day(current),
        initial=captured,
    )
    numbered_days = enumerate(campaign, start=1)
    completed_days = filter(
        lambda day: len(day[1]) == n * m,
        numbered_days,
    )
    return next(completed_days)[0]


def conquest_campaign(n, m, l, battalion):
    coordinates = battalion[:l * 2]
    captured = set(zip(coordinates[::2], coordinates[1::2]))
    return count_days(n, m, captured)


def main():
    result = conquest_campaign(3, 4, 2, [2, 2, 3, 4])
    print("Полигон будет полностью захвачен на день: " + str(result))


if __name__ == "__main__":
    main()
