#Grading system code:

students_score = {
  "Aman":81,
  "Kailash":74,
  "Abhinav":99,
  "Kapil":62,
}
students_grades={}
for grades in students_score:
  system=students_score[grades]
  print(system)
  if system>90:
    students_grades[grades]="Your grades are fantestic"
  elif system>80 and system<90:
    students_grades[grades]="Your grades are good"
  elif system>70 and system<80:
     students_grades[grades]="Your can improve"
  elif system>60 and system<70:
     students_grades[grades]="Your grades are bad need to improve them"

print(students_grades)












