puzzle = 2.60
talking_doll = 3.0
teddy_bear = 4.10
minion = 8.20
truck = 2.0

vacation = float(input())

amount_puzzles = int(input())
amount_talking_doll = int(input())
amount_teddy_bear = int(input())
amount_minion = int(input())
amount_truck = int(input())

toys_total_pc = amount_truck + amount_puzzles + amount_minion + amount_teddy_bear + amount_talking_doll

bill = amount_puzzles * puzzle
bill += amount_talking_doll * talking_doll
bill += amount_teddy_bear * teddy_bear
bill += amount_minion * minion
bill += amount_truck * truck

if toys_total_pc >= 50:
    bill = bill - (bill * (25 / 100))

bill -= (bill * (10 / 100))

if bill >= vacation:
    remaining = bill - vacation
    print(f'Yes! {remaining:.2f} lv left.')
else:
    remaining = vacation - bill
    print(f'Not enough money! {remaining:.2f} lv needed.')
