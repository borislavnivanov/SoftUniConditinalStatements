volume_pool = int(input())
pipe_1_debit = int(input())
pipe_2_debit = int(input())
hours = float(input())

pipe_1_total = pipe_1_debit * hours
pipe_2_total = pipe_2_debit * hours
total_debit = pipe_1_total + pipe_2_total

pool_full = (total_debit / volume_pool) * 100
p1_usage = (pipe_1_total / total_debit) * 100
p2_usage = (pipe_2_total / total_debit) * 100

if pool_full <= 100:
    print(f'The pool is {pool_full:.2f}% full. Pipe 1: {p1_usage:.2f}%. Pipe 2: {p2_usage:.2f}%.')
else:
    print(f'For {hours:.2f} hours the pool overflows with {abs(volume_pool - total_debit):.2f} liters.')
