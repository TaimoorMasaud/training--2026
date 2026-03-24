def calculate_average(scores):
    return sum(scores) / len(scores) if scores else 0


def get_grade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B'
    elif avg >= 70:
        return 'C'
    elif avg >= 60:
        return 'D'
    else:
        return 'F'


def class_topper(students):
    return max(students, key=lambda s: calculate_average(s['scores']))


# Data: list of students
students = [
    {"name": "Ali", "scores": [85, 90, 88], "subject": "Math"},
    {"name": "Sara", "scores": [92, 95, 94], "subject": "Science"},
    {"name": "Ahmed", "scores": [70, 75, 72], "subject": "History"},
    {"name": "Ayesha", "scores": [88, 84, 86], "subject": "English"},
    {"name": "Bilal", "scores": [60, 65, 63], "subject": "Geography"},
]

# Find topper
topper = class_topper(students)

# Create a sorted copy (without modifying original list)
sorted_students = sorted(
    students,
    key=lambda s: calculate_average(s['scores']),
    reverse=True
)


print("Student Report")
print("-" * 50)
print(f"{'Name':<10} {'Avg Score':<12} {'Grade':<6}")
print("-" * 50)

for s in sorted_students:
    avg = calculate_average(s['scores'])
    grade = get_grade(avg)
    
    line = f"{s['name']:<10} {avg:<12.2f} {grade:<6}"
    
    if s == topper:
        line += " *** TOP ***"
    
    print(line)