player = {
    'name': input('Ваше имя: '),
    'health': 100,
    'damage': 32,
    'armor': 1.4,
}

enemy = {
    'name': 'Бот',
    'health': 100,
    'damage': 51,
    'armor': 1.2,
}


def attack(person1: dict, person2: dict):
    def damage():
        return person1['damage'] / person2['armor']

    person2['health'] -= damage()

    print(person1, person2)


attack(player, enemy)
