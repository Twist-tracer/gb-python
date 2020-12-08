numbers = [1, -4, 15, 17, 51, 24, 0, -32, 16, -17, -11]

new_numbers = [number for number in numbers if ((number % 3) == 0) and (number > 0) and ((number % 4) != 0)]

print(new_numbers)
