import math

grapes_plantation_size = int(input())
grapes_output_per_m2 = float(input())
wine_target_l = int(input())
workers = int(input())

LITTER_WINE = 2.5
RESERVATION_WINE = 40 / 100

wine_production_output = ((grapes_plantation_size * grapes_output_per_m2) * RESERVATION_WINE) / LITTER_WINE

if wine_production_output < wine_target_l:
    print(f'It will be a tough winter! More {math.floor(wine_target_l - wine_production_output)} liters wine needed.')
else:
    wine_reminder = math.ceil(wine_production_output - wine_target_l)
    print(f'Good harvest this year! Total wine: {wine_production_output:.0f} liters.\n{wine_reminder} liters left -> {math.ceil(wine_reminder / workers)} liters per person.')
