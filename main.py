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

print(group_json)
print(group_pickle)

with open('group.json', 'w', encoding='utf-8') as file:
    json.dump(group_json, file)

with open('group.pickle', 'wb') as file:
    pickle.dump(group_pickle, file)
