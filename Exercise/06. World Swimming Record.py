current_record = float(input())
length_m = float(input())
time_for_m = float(input())

time = length_m * time_for_m

resistance = 12.5 * (length_m // 15)
time += resistance

if time < current_record:
    print(f'Yes, he succeeded! The new world record is {time:.2f} seconds.')
else:
    print(f'No, he failed! He was {time - current_record:.2f} seconds slower.')
