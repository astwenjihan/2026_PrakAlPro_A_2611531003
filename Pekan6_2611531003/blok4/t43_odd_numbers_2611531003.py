# Expected output: 1, 3, 5 (one per line)
number_1003 = 1

while number_1003 <= 6:
       if number_1003 % 2 == 0:
             number_1003 += 1
             continue
       print(number_1003)
       number_1003 += 1