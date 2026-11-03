# Expected output: 1, 3, 5 (one per line)
number = 1
while number <= 6:
   if number % 2 == 0:
        continue
   print(number)
   number += 1


for number in range(1, 8):
   if number % 4 == 0:
        break
   print(number)


for number in range(1, 8):
   if number % 4 == 0:
        continue
   print(number)


for row in range(1, 4):
    for column in range(1, 4):
        if column == 2:
            break
        print(row, column)