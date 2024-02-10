budget = float(input())
videocard_pc = int(input())
processor_pc = int(input())
ram_pc = int(input())

price_videocard = 250.00 * videocard_pc
price_processor = (price_videocard * (35 / 100)) * processor_pc
price_ram = (price_videocard * (10 / 100)) * ram_pc

bill = price_videocard + price_processor + price_ram

if videocard_pc > processor_pc:
    bill -= bill * (15 / 100)

if bill <= budget:
    print(f'You have {budget - bill:.2f} leva left!')
else:
    print(f'Not enough money! You need {bill - budget:.2f} leva more!')