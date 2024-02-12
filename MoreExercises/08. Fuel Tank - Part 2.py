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
has_club_card = 'True' if input() == 'Yes' else 'False'

bill = float(0)


def get_billed():
    price = 0
    if type_of_fuel == 'Gasoline':
        price += volume_loaded * GASOLINE
    elif type_of_fuel == 'Diesel':
        price += volume_loaded * DIESEL
    elif type_of_fuel == 'Gas':
        price += volume_loaded * GAS
    return price


if has_club_card == "True":
    bill += get_billed()
    if type_of_fuel == 'Gasoline':
        bill -= volume_loaded * DISCOUNT_GASOLINE
    elif type_of_fuel == 'Diesel':
        bill -= volume_loaded * DISCOUNT_DIESEL
    elif type_of_fuel == 'Gas':
        bill -= volume_loaded * DISCOUNT_GAS
else:
    bill += get_billed()

if volume_loaded > 25:
    bill -= bill * DISCOUNT_OVER_25
elif volume_loaded >= 20:
    bill -= bill * DISCOUNT_20_to_25

print(f'{bill:.2f} lv.')
