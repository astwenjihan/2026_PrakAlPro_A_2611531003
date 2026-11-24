menus = ["Nasi Goreng", "Mie Ayam", "Soto"]
number_of_days = 3
sales = []

for i in range(number_of_days):
    row = []
    for menu in menus:
        jumlah = int(input(f"Day {i + 1}, {menu}: "))
        row.append(jumlah)
    sales.append(row)

print('Total per day: ')
for r in range(len(sales)):
    total_hari = 0
    for c in range(len(sales[r])):
        total_hari += sales [r][c]
    print(f"Day {r + 1}: {total_hari}")

menu_totals = []
for c in range(len(menus)):
    total_menu = 0
    for r in range(len(sales)):
        total_menu += sales[r][c]
    menu_totals.append((menus[c], total_menu))

terlaris_nama = menu_totals[0][0]
terlaris_jumlah = menu_totals[0][1]

for nama, total in menu_totals:
    if total > terlaris_jumlah:
        terlaris_jumlah = total
        terlaris_nama = nama

print(f'Best Seller: {terlaris_nama}, ({terlaris_jumlah})')