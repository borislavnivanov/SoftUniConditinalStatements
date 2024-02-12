travel_km = int(input())
travel_time = input()

TAXI_BASE = 0.70
TAXI_DAY = 0.79
TAXI_NIGHT = 0.90

AUTOBUS = 0.09
TRAIN = 0.06

bill = 0

if travel_km >= 100:
    bill = travel_km * TRAIN
elif travel_km >= 20:
    bill = travel_km * AUTOBUS
else:
    bill += TAXI_BASE
    if travel_time == 'day':
        bill += travel_km * TAXI_DAY
    else:
        bill += travel_km * TAXI_NIGHT

print(f'{bill:.2f}')
