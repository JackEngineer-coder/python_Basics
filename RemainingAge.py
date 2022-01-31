#code for calculating remaining age
current_age = input("enter your age\n")

Total_days = 90*365
Total_month = 90*12
Total_week = 90*52
Remaining_days = Total_days - int(current_age)*365
Remaining_month = Total_month - int(current_age)*12
Remaining_week = Total_week - int(current_age)*52
#f-string it saves times of conversion to print various things in python
print(f"your remaining days are - {Remaining_days}, your remaining months are - {Remaining_month}, Your remaining weeks are - {Remaining_week}")




