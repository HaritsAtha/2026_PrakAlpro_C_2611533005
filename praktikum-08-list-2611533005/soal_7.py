menus = ["Nasi Goreng", "Mie Ayam", "Soto"]
number_of_days = 3
sales = []
# Write your code below
for i in range(number_of_days):
    row = []
    for menu in menus:
        amount = int(input(f"Day {i + 1}, {menu}: "))
        row.append(amount)
    sales.append(row)

print("Total per day:")
for i in range(number_of_days):
    total = 0
    for j in range(len(menus)):
        total += sales[i][j]
    print(f"Day {i + 1}: {total}")

menu_totals = []

for j in range(len(menus)):
    total = 0
    for i in range(number_of_days):
        total += sales[i][j]
    menu_totals.append((menus[j], total))

print("Total per menu:", menu_totals)

best_seller = menu_totals[0]

for name, total in menu_totals:
    if total > best_seller[1]:
        best_seller = (name, total)

print("Best seller:", best_seller)