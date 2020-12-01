import random

variant = None
variants = ['<', '>', '=']
min_number = 0
max_number = 100
number = random.randint(min_number, max_number)

while variant != '=':
    print(f'Я думаю это число {number}, правильно?')

    print(
        'Выберете один из вариантов ответа:',
        '> - число больше',
        '< - число меньше',
        '= - правильно',
        sep='\n'
    )

    variant = input('Ваш вариант: ')
    while variant not in variants:
        print('Введен некорректный вариант, попробуйте еще раз')
        variant = input('Ваш вариант: ')

    if variant == '<':
        min_number = number
    elif variant == '>':
        max_number = number

    number = int(min_number + ((max_number - min_number) / 2))
else:
    print('Ура!')
