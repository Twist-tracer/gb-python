my_list_1 = [2, 2, 5, 12, 8, 2, 12]
my_set_1 = set(my_list_1)

result = []
for set_item in my_set_1:
    set_items_from_list = []

    for list_item in my_list_1:
        if set_item == list_item:
            set_items_from_list.append(list_item)

    if len(set_items_from_list) == 1:
        result.append(set_item)


print(result)
