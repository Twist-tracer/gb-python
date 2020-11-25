while True:
    number = int(input('Введите число больше 0, но меньше 10: '))
    if (number > 0) and (number < 10):
        break
    elif number <= 0:
        print('Ваше число должно быть больше 0')
    else:
        print('Ваше число должно быть меньше 10')


number = number ** 2

print('Ваше число в квадрате будет ' + str(number))
