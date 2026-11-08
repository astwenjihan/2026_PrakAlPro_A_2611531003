PASS_SCORE_1003 = 60

while True:
    num_students_1003 = int(input("Number of students: "))
    if num_students_1003 >= 1:
        break
    print("Invalid student count !")
total_score_1003 = 0
passed_count_1003 = 0
highest_score_1003 = 0

for i_1003 in range (1, num_students_1003 + 1):
    print("Student: ", i_1003)

    while True:
        score_1003 = int(input("Enter score: "))
        if 0 <= score_1003 <= 100:
            break
        print("Invalid score !")

    total_score_1003 += score_1003

    if score_1003 >= PASS_SCORE_1003:
        passed_count_1003 += 1

    if i_1003 == 1 or score_1003 > highest_score_1003:
        highest_score_1003 = score_1003

average_score_1003 = total_score_1003 / num_students_1003

print('Total score: ', total_score_1003)
print('Average score: ', round(average_score_1003, 2))
print('Passed count: ', passed_count_1003)
print('Highest score: ', highest_score_1003)