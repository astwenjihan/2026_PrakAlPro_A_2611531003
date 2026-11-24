number_rows = 4
seats_row = 5

board = []
for i in range(number_rows):
    row = []
    for j in range(seats_row):
        row.append('.')
    board.append(row)

while True:
    for i in range(number_rows):
        line = f"Row {i+1}: "
        for j in range(seats_row):
            line += f"{board[i][j]} "
        print(line)

    row_choice = int(input('Row (0 to stop): '))
    if row_choice == 0:
        break

    seat_choice = int(input("Seat: "))

    if (
        row_choice < 1
        or row_choice > number_rows
        or seat_choice < 1
        or seat_choice > seats_row
    ):
        print("Invalid seat.")
    elif board[row_choice - 1][seat_choice - 1] == 'X':
        print("Seat already taken.")
    else:
        board[row_choice - 1][seat_choice - 1] = 'X'
        print('Seat booked.')

seats_taken = 0
for i in range(number_rows):
    for j in range(seats_row):
        if board[i][j] == 'X':
            seats_taken += 1

print('Seats taken: ', seats_taken)