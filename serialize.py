import json, pickle

my_favourite_group = {
    'name': 'Г.М.О.',
    'tracks': ['Последний месяц осени', 'Шапито'],
    'Albums': [
        {'name': 'Делать панк-рок', 'year': 2016},
        {'name': 'Шапито', 'year': 2014}
   ]
}

group_json = json.dumps(my_favourite_group)
group_pickle = pickle.dumps(my_favourite_group)

print(type(group_json), group_json)
print(type(group_json), group_pickle)

with open('group.json', 'w', encoding='utf-8') as file:
    json.dump(my_favourite_group, file)

with open('group.pickle', 'wb') as file:
    pickle.dump(my_favourite_group, file)
