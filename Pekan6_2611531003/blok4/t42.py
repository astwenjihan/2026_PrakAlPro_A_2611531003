for number in range(1, 8):
    if number % 4 == 0:
        break
    print(number)

print("======")

for number in range(1, 8):
    if number % 4 == 0:
        continue
    print(number)

print("======")

for row in range(1, 4):
    for column in range(1, 4):
        if column == 2:
            break
        print(row, column)