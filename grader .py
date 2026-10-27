mark = float(input("Enter the student's mark: "))

if mark >= 70:
	grade = "A"
elif mark >= 60:
	grade = "B"
elif mark >= 50:
	grade = "C"
elif mark >= 40:
	grade = "D"
else:
	grade = "Fail"

print(f"Grade: {grade}")