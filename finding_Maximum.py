#code for finding the maximum number:

student_marks= input("enter students marks using comma\n").split(",")

for n in range(0,len(student_marks)):
  student_marks[n] = int(student_marks[n])
print(student_marks)

highest_marks = 0
for marks in student_marks:
  if highest_marks<marks:
    highest_marks= marks
print(f"Highest marks is {highest_marks}")

