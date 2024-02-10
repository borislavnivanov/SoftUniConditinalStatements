base_score = int(input())
bonus = 0

if base_score > 1000:
    bonus = base_score * (10 / 100)
elif base_score > 100:
    bonus = base_score * (20 / 100)
else:
    bonus += 5

if base_score % 2 == 0:
    bonus += 1
elif base_score % 10 == 5:
    bonus += 2

print(bonus)
print(base_score + bonus)
