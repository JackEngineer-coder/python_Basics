#Tip calculator project

print("Welcome to Tip Calculator\n")
Total_bill = input("What was the total bill?\n")
Tip_percentage =input("What amount of percentage tip you want to give - 10, 12 or 15?\n")
Total_people = input("How many people to split the bill?\n")
tip_amount = float(Total_bill)* float(Tip_percentage)/100
Total_bill_with_tip = float(tip_amount) + float(Total_bill)
split_bill = float(Total_bill_with_tip)/int(Total_people) 
split_bill_roundoff= int(round(split_bill))
print(f"Each person should pay:{split_bill_roundoff} ")
