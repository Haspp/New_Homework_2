import math


array = [1, 2, 3, 4, 5]
result = []

for i in range(int(len(array))):
    result.append(math.factorial(array[i]))
    print(f'Факториал {array[i]}! = {result}')


# while i in range(len(array)):
#     print(f'*{i}', end='')
#     i += 1

