import math

series_name = input()
series_runtime = int(input())
break_time = int(input())

break_deductions = break_time / 8
break_time -= break_deductions * 1  #lunch
break_time -= (break_deductions * 2)  #relax

if series_runtime <= break_time:
    result = break_time - series_runtime
    result = math.ceil(result)
    print(f'You have enough time to watch {series_name} and left with {result} minutes free time.')
else:
    result = series_runtime - break_time
    result = math.ceil(result)
    print(f'You don\'t have enough time to watch {series_name}, you need {result} more minutes.')
