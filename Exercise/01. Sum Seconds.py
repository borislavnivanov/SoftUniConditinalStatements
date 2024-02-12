time_first = int(input())
time_second = int(input())
time_third = int(input())

total_times = time_first + time_second + time_third

# minutes = (datetime.timedelta(seconds=total_times))

minutes = total_times // 60
seconds = total_times % 60

print(f'{minutes}:{seconds:02d}')

# if seconds < 10:
#     print(f'{minutes}:0{seconds}')
# else:
#     print(f'{minutes}:{seconds}')
