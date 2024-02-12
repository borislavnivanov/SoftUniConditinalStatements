import math

MAGNOLIAS = 3.25
HYACINTH = 4
ROSE = 3.50
CACTUS = 8
REVENUE_TAX = 5 / 100

pc_magnolias = int(input())
pc_hyacinth = int(input())
pc_rose = int(input())
pc_cactus = int(input())
present_price = float(input())

sale_revenue = (
    pc_cactus * CACTUS +
    pc_hyacinth * HYACINTH +
    pc_rose * ROSE +
    pc_magnolias * MAGNOLIAS
)

sale_revenue -= sale_revenue * REVENUE_TAX

remainder = sale_revenue - present_price

if remainder >= 0:
    print(f'She is left with {math.floor(remainder):.0f} leva.')
else:
    print(f'She will have to borrow {math.ceil(abs(remainder)):.0f} leva.')
