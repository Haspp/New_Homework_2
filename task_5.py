import random

N = int(input('Введите длину списка: '))
list_user = []

for i in range(N):
    list_user.append(random.randint(-N, N))
print(list_user)

random.shuffle(list_user)

print(f'Перемешанный список: {list_user}')
