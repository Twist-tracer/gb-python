def person(name, age, city):
    return f'{name}, {age} год(а), проживает в городе {city[0].upper()}{city[1:]}'

print(person('Василий', 21, 'москва'))
