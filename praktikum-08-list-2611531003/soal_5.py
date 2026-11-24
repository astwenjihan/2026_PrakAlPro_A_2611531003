# Attendance board: 3 students x 4 meetings, 0 = absent
board = [[0] * 4 for i in range(3)]
board[0][1] = 1  # student 1 is present at meeting 2
board[2][3] = 1  # student 3 is present at meeting 4
for row in board:
    print(row)