total_1003 = 0

while True:
    number_1003 = int(input("Enter a number: "))

    if number_1003 < 0:
        break
    if number_1003 == 0:
        continue

    print("Positive number:", number_1003)
    total_1003 += number_1003

print("Total:", total_1003)