import random


def get_rand_item(items: list):
    if len(items) <= 0:
        return None

    return random.choice(items)

# print(l.get_rand_item([1, 2, 3, 4]))
