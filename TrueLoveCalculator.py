# # True love calculator
print("Welcome to Love Calculator\n")
first_Name = input("Enter Your Name\n")
Second_Name = input("Enter Your Partner Name\n")
lower_first_name = first_Name.lower()
lower_second_name = Second_Name.lower()
Combined_string = lower_first_name+lower_second_name
t=Combined_string.count("t")
r=Combined_string.count("r")
u=Combined_string.count("u")
e=Combined_string.count("e")
TRUE = t+r+u+e

l=Combined_string.count("l")
o=Combined_string.count("o")
v=Combined_string.count("v")
e=Combined_string.count("e")

Love = l+o+v+e
True_lov= str(TRUE)+str(Love)
True_love = int(True_lov)

if True_love<= 20:
  print(f"you are like coke and mentos, your true love is {True_love}%")
elif True_love>20 and True_love<= 40:
  print(f"you are alright together, your true love is {True_love}%")
elif True_love>40:
  print(f"your True love is {True_love}%, Congratulations")




