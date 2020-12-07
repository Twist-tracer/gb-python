import json, pickle

with open('group.json', 'r', encoding='utf-8') as file:
    my_favourite_group = json.load(file)
    print(type(my_favourite_group), my_favourite_group)

with open('group.pickle', 'rb') as file:
    my_favourite_group = pickle.load(file)
    print(type(my_favourite_group), my_favourite_group)
