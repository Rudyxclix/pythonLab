# Experiment 9: Student Performance Analysis

## Aim
To use functions and a lambda expression to analyze marks in three subjects for each student.

## Algorithm
1. Read each student's name and three marks.
2. Use functions to calculate total, average, and grade.
3. Find the highest and lowest individual marks across the entered students.
4. Sort students by total marks using a lambda expression.

## Grade criteria
- A: average 90 or above
- B: average 75 to less than 90
- C: average 60 to less than 75
- D: average 40 to less than 60
- F: average below 40

## Sample input
```text
2
Anu
80
90
85
Ravi
70
75
80
```

## Sample output
```text
Anu - Total: 255.0 Average: 85.00 Grade: B
Ravi - Total: 225.0 Average: 75.00 Grade: B
Highest mark: 90.0
Lowest mark: 70.0
Students sorted by total marks:
Anu 255.0
Ravi 225.0
```

## Explanation
The helper functions handle the calculations. The lambda expression supplies the total-mark sorting key.
