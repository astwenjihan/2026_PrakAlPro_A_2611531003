# Expected output: 3 rows, each row has 4 stars.
for row in range(1, 4):
    for column in range(1, 5):
        print("*", end=" ")
    print()