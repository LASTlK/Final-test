#Задание 3

'''print('Введите три числа: ')
x = int(input())
y = int(input())
z = int(input())
print(f'{x} + {y} + {z} = {x + y + z}')'''

# Задание 4

'''print('Введите три числа: ')
x = int(input())
y = int(input())
z = int(input())
print(f'{x} + {y} + {z} = {x + y + z}')
print(f'{x} * {y} * {z} = {x * y * z}')'''

#Задание 5

'''print('Введите три числа: ')
x = int(input())
y = int(input())
z = int(input())
print(f'{x} + {y} + {z} = {x + y + z}')
print(f'{x} * {y} * {z} = {x * y * z}')
print(f'{x} + {y} + {z} = {(x + y + z) / 3}')'''

#Задание 4 с ветвлением

print('Введите номер месяца: ')
x = int(input())
if x == 1 or x == 2 or x == 12:
    print('Зима')
elif x == 3 or x == 4 or x == 5:
    print('Весна')
elif x == 6 or x == 7 or x == 8:
    print('Лето')
elif x == 9 or x == 10 or x == 11:
    print('Осень')
else:
    print('Неверный номер месяца')

