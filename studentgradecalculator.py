marks = list(map(int, input("Enter marks: ").split()))

total = sum(marks)
average = total / len(marks)
percentage = (total / (len(marks) * 100)) * 100

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

if percentage >= 40:
    result = "Pass"
else:
    result = "Fail"

print("\n===== STUDENT GRADE CALCULATOR =====")
print("Total Marks :", total)
print("Average     :", round(average, 2))
print("Percentage  :", round(percentage, 2), "%")
print("Grade       :", grade)
print("Result      :", result)