# code for calculating average height of the students of a class:
student_heights = input("Input a list of student heights\n ").split(",")

for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
print(student_heights)

total=0
for height in student_heights:
  total+=height
print(total)

student_count=0
for student in student_heights:
  student_count+=1
print(student_count)

average=round(total/student_count)
print(average)


