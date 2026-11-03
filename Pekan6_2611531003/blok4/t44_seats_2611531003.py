blocked_seat_1003 = 3

for row_1003 in range(1, 4):
    print("Row", row_1003, end=": ")
    for seat_1003 in range(1, 6):
        if seat_1003 == blocked_seat_1003:
            break
        print(seat_1003, end=" ")
    print()