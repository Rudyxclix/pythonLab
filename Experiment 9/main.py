def calculate_total(marks):
    return sum(marks)


def calculate_average(marks):
    return calculate_total(marks) / len(marks)


def find_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"


number_of_students = int(input("Enter the number of students: "))
students = []

for count in range(number_of_students):
    name = input("Enter student name: ")
    marks = []
    for subject in range(3):
        mark = float(input("Enter mark for subject " + str(subject + 1) + ": "))
        marks.append(mark)
    students.append({"name": name, "marks": marks})

all_marks = []
for student in students:
    total = calculate_total(student["marks"])
    average = calculate_average(student["marks"])
    grade = find_grade(average)
    student["total"] = total
    all_marks.extend(student["marks"])
    print(
        student["name"],
        "- Total:", total,
        "Average:", format(average, ".2f"),
        "Grade:", grade,
    )

if all_marks:
    print("Highest mark:", max(all_marks))
    print("Lowest mark:", min(all_marks))

students.sort(key=lambda student: student["total"], reverse=True)
print("Students sorted by total marks:")
for student in students:
    print(student["name"], student["total"])
