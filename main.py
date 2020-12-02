player = {
    'name': input('Ваше имя: '),
    'health': 100,
    'damage': 32,
    'armor': 1.4,
}

enemy = {
    'name': input('Имя врага: '),
    'health': 100,
    'damage': 51,
    'armor': 1.2,
}


def get_damage(damage, armor):
    return damage / armor


def attack(unit: dict, target: dict):
    target['health'] -= get_damage(unit['damage'], target['armor'])


attack(player, enemy)

print(enemy)
