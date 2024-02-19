type_of_fuel = input()
fuel_in_tank = float(input())

if type_of_fuel == "Diesel" or type_of_fuel == "Gasoline" or type_of_fuel == "Gas":
    type_of_fuel = type_of_fuel.lower()
    if fuel_in_tank >= 25:
        print(f'You have enough {type_of_fuel}.')
    else:
        print(f'Fill your tank with {type_of_fuel}!')
else:
    print('Invalid fuel!')

# if fuel_in_tank >= 25:
#     if type_of_fuel == 'Diesel':
#         print(f'You have enough diesel.')
#     elif type_of_fuel == 'Gasoline':
#         print(f'You have enough gasoline.')
#     elif type_of_fuel == 'Gas':
#         print(f'You have enough gas.')
#     else:
#         print('Invalid fuel!')
# else:
#     if type_of_fuel == 'Diesel':
#         print(f'Fill your tank with diesel!')
#     elif type_of_fuel == 'Gasoline':
#         print(f'Fill your tank with gasoline!')
#     elif type_of_fuel == 'Gas':
#         print(f'Fill your tank with gas!')
#     else:
#         print('Invalid fuel!')
