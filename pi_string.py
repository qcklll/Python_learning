filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line

birthday = input("Введите вашу дату рождения в формате mmddyy")
if birthday in pi_string:
    print("Ваше день рождение есть в миллионе цифр числа пи")
else:
    print("Вашего дня рождения нет в миллионе цифр числа пи")