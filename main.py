firstname = input('Ваше имя: ')
lastname = input('Ваша фамилия: ')
age = int(input('Ваш возраст: '))
weight = int(input('Ваш вес: '))

if (age < 30) and ((weight >= 50) and (weight < 120)):
    print(firstname, lastname + ',', age, 'год,', 'вес', weight, '- хорошее состояние')
elif (age > 40) and ((weight < 50) or (weight > 120)):
    print(firstname, lastname + ',', age, 'год,', 'вес', weight, '- следует обратится к врачу!')
elif (age > 30) and ((weight < 50) or (weight > 120)):
    print(firstname, lastname + ',', age, 'год,', 'вес', weight, '- следует заняться собой')
else:
    print('Пациент на мой вкус и полет фантазии')
