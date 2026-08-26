from functools import reduce


def add_segment(state, segment):
    total_distance, previous_time = state
    speed, current_time = segment
    segment_time = current_time - previous_time
    new_distance = total_distance + speed * segment_time
    return new_distance, current_time


def odometer(oksana):
    values = iter(oksana)
    segments = zip(values, values)
    total_distance, _ = reduce(add_segment, segments, (0, 0))
    return total_distance


def main():
    result = odometer([10, 1, 20, 2])
    print("Пройденное расстояние: " + str(result) + " км")


if __name__ == "__main__":
    main()
