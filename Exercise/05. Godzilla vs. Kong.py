film_budget = float(input())
extras = int(input())
price_cloths_extra = float(input())

film_budget -= film_budget * (10 / 100)

cloths = extras * price_cloths_extra

if extras > 150:
    cloths -= cloths * (10 / 100)

film_budget -= cloths

if film_budget >= 0:
    print(f'Action!\nWingard starts filming with {film_budget:.2f} leva left.')
else:
    film_budget = film_budget - 2 * film_budget
    print(f'Not enough money!\nWingard needs {film_budget:.2f} leva more.')
