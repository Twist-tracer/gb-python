def squares(number: int):
    if number < 1 or number > 100:
        raise ValueError('Введите число от 1 до 100')

    if number == 13:
        raise ValueError('Вы ввели запрещенное число!')

    return number**2


number = int(input('Введите число: '))

try:
    print(squares(number))
except ValueError as e:
    print(e)
