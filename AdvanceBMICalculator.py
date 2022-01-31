#advance BMI calculator
weight = int(input("Enter your weight\n"))
height = float(input("Enter you height\n"))
BMI = int(weight)/float(height)**2
new_BMI = float(BMI) 
if new_BMI<18:
 print("YOu are under weight")
elif 25 >= new_BMI >= 18: 
 print("you are normal")
elif new_BMI > 25 and new_BMI <= 35:
 print("you are obese")
elif new_BMI > 35:
 print("you are clinically obese")

else:
 print("Invalid Entries") 
