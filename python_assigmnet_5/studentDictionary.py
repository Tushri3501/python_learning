student_marks = {"Amit":85, "Sneha":92, "Rahul":78, "Priya":88, "Karen":73}
name = input("Enter the student name: ")
if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print(f"Student named '{name}' not found in the records.")