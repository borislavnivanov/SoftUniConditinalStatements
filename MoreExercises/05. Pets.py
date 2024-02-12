import math

travel_days = int(input())
preped_food = int(input())

food_per_day_dog = float(input())
food_per_day_cat = float(input())
food_per_day_turtle = float(input()) / 1000

needed_food = (
    food_per_day_dog * travel_days +
    food_per_day_cat * travel_days +
    food_per_day_turtle * travel_days
)

if needed_food <= preped_food:
    print(f'{math.floor(preped_food - needed_food)} kilos of food left.')
else:
    print(f'{math.ceil(abs(preped_food - needed_food))} more kilos of food are needed.')
