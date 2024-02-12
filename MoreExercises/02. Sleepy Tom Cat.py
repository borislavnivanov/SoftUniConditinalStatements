PLAY_MAX = 30000
PLAY_WHEN_WORK = 63
PLAY_WHEN_OFF = 127

holidays = int(input())

total_play_time = (365 - holidays) * PLAY_WHEN_WORK
total_play_time += holidays * PLAY_WHEN_OFF

total_play_time -= PLAY_MAX

hours = abs(total_play_time) // 60
minutes = abs(total_play_time) % 60

if total_play_time > 0:
    print(f'Tom will run away\n{hours} hours and {minutes} minutes more for play')
else:
    print(f'Tom sleeps well\n{hours} hours and {minutes} minutes less for play')
