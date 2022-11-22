import math

x = int(input('Введите координату х = '))
y = int(input('Введите координату y = '))
x1 = int(input('Введите координату х1 = '))
y1 = int(input('Введите координату y1 = '))

distance = math.sqrt((x1-x) ** 2 + (y1-y) ** 2)

print(f'Расстояние между точками А и Б в системе координат {distance}')
