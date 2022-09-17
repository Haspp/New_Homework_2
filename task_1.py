# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#
# Пример:
#
# - 0,56 -> 11

number = float(input('Введите вещественное число: '))
str_number = str(number)
str_number = str_number.replace('.', '')
list_str = list(str_number)
list_num = map(int, list_str)
s = sum(list_num)

print(s)


