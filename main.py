date = '02.11.2000'

days = {
    '01': 'первое',
    '02': 'второе',
    '03': 'третье',
}

months = {
    '09': 'сентября',
    '10': 'октября',
    '11': 'ноября',
}

date_parts = date.split('.')

print(days[date_parts[0]], months[date_parts[1]], date_parts[2], 'года')
