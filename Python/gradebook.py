# gradebook.py

# Display the average of each student's grade.


# Display the average for each assignment.

gradebook = [[61, 74, 69, 62, 72, 66, 73, 65, 60, 63, 69, 63, 62, 61, 64],
             [73, 80, 78, 76, 76, 79, 75, 73, 76, 74, 77, 79, 76, 78, 72],
             [90, 92, 93, 92, 88, 93, 90, 95, 100, 99, 100, 91, 95, 99, 96],
             [96, 89, 94, 88, 100, 96, 93, 92, 94, 98, 90, 90, 92, 91, 94],
             [76, 76, 82, 78, 82, 76, 84, 82, 80, 82, 76, 86, 82, 84, 78],
             [93, 92, 89, 84, 91, 86, 84, 90, 95, 86, 88, 95, 88, 84, 89],
             [63, 66, 55, 67, 66, 68, 66, 56, 55, 62, 59, 67, 60, 70, 67],
             [86, 92, 93, 88, 90, 90, 91, 94, 90, 86, 93, 89, 94, 94, 92],
             [89, 80, 81, 89, 86, 86, 85, 80, 79, 90, 83, 85, 90, 79, 80],
             [99, 73, 86, 77, 87, 99, 71, 96, 81, 83, 71, 75, 91, 74, 72]]

average_student = []
count = 0
for row in gradebook:
    average_student.append(0)
    for x in row:
        average_student[count] += x
    average_student[count] /= len(row)
    count += 1


total_assignment = [sum(column) for column in zip(*gradebook)]
average_assignment = [column_sum / len(gradebook) for column_sum in total_assignment]

print("Assignment Averages:\n")
for i, average in enumerate(average_assignment, start = 1):
    print(f"Assignment {i}: {average: .2f}\n")
for j, avg in enumerate(average_student, start = 1):
    print(f"Student {j}: {avg: .2f}\n")


