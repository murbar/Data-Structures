import random


def random_walk(n):
    """Return coordinates after N radmon walks"""
    x, y = 0, 0
    for i in range(n):
        (dx, dy) = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        x += dx
        y += dy

    return x, y


# monte carlo sim
number_of_walks = 10_000
for walk_len in range(1, 31):
    less_than_4_away = 0
    for i in range(number_of_walks):
        x, y = random_walk(walk_len)
        distance = abs(x) + abs(y)
        if distance <= 4:
            less_than_4_away += 1
    percentage = float(less_than_4_away) / number_of_walks
    print(f"Walk size {walk_len} - {percentage * 100}% less than 4 away")
