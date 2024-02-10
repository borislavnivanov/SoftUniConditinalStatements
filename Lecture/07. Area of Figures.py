from math import pi

type_of_figure = input()
area = float()

match type_of_figure:
    case 'square':
        side = float(input())
        area = side ** 2
        # print(f'{area:.3f}')

    case 'rectangle':
        side_a = float(input())
        side_b = float(input())
        area = side_a * side_b
        # print(f'{area:.3f}')

    case 'circle':
        radius = float(input())
        area = (radius ** 2) * pi
        # print(f'{area:.3f}')

    case 'triangle':
        side = float(input())
        h = float(input())
        area = (side * h) / 2
        # print(f'{area:.3f}')

print(f'{area:.3f}')
