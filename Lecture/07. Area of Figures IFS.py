from math import pi

type_of_figure = input()

if type_of_figure == 'square':
    side = float(input())
    area = side ** 2
    print(f'{area:.3f}')
elif type_of_figure == 'rectangle':
    side_a = float(input())
    side_b = float(input())
    area = side_a * side_b
    print(f'{area:.3f}')
elif type_of_figure == 'circle':
    radius = float(input())
    area = (radius ** 2) * pi
    print(f'{area:.3f}')
elif type_of_figure == 'triangle':
    side = float(input())
    h = float(input())
    area = (side * h) / 2
    print(f'{area:.3f}')
