import random

N = int(input('Введите длину списка: '))
list_user = []

for i in range(N):
    list_user.append(random.randint(-N, N))
print(list_user)

list_i = input('Введите элемнты списка:')

if list_i != '':
    list_i = list_i.replace('.', ' ').replace(',', ' ').split()
    result = 1

    for i in range((len(list_i))):
        if int(list_i[i]) < len(list_user):
            result *= list_user[int(list_i[i])]
    print(result)
else:
    print(0)

