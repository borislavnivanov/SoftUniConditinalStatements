GASOLINE = 2.22
DIESEL = 2.33
GAS = 0.93

# discount per litter
DISCOUNT_GASOLINE = 0.18
DISCOUNT_DIESEL = 0.12
DISCOUNT_GAS = 0.08
# discounts of total price
DISCOUNT_20_to_25 = 8 / 100
DISCOUNT_OVER_25 = 10 / 100

type_of_fuel = input()
volume_loaded = float(input())
has_club_card = True if input() == 'Yes' else False


def get_card_discount(fuel: str = type_of_fuel):
    discount = 0
    if fuel == 'Gasoline':
        discount += volume_loaded * DISCOUNT_GASOLINE
    elif fuel == 'Diesel':
        discount += volume_loaded * DISCOUNT_DIESEL
    elif fuel == 'Gas':
        discount += volume_loaded * DISCOUNT_GAS
    return discount


def get_billed(fuel: str = type_of_fuel):
    price = 0
    if fuel == 'Gasoline':
        price += volume_loaded * GASOLINE
    elif fuel == 'Diesel':
        price += volume_loaded * DIESEL
    elif fuel == 'Gas':
        price += volume_loaded * GAS
    return price


bill = get_billed(type_of_fuel)

if has_club_card:
    bill -= get_card_discount(type_of_fuel)

if volume_loaded > 25:
    bill -= bill * DISCOUNT_OVER_25
elif volume_loaded >= 20:
    bill -= bill * DISCOUNT_20_to_25

print(f'{bill:.2f} lv.')
