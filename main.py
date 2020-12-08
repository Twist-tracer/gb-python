from math import sqrt


def squares(items: list):
    return [round(sqrt(item)) if item > 1 else item for item in items]


numbers = [1, -4, 15, 17, 51, 24, 0, -32, 16, -17, -11]

print(squares(numbers))
