#pizza order app

print("Welcome to pizza Store\n")
size = input("What size of pizza do you want? Samll, Medium and Large\n")
pepperoni = input("Do you want to add pepperoni? yes, NO\n")
if size == 'S':
   price = 15
  
if size == 'M':
   price = 20
  
if size== "L":
   price = 25
  



if pepperoni =='Y':
  if size =='S':
   price+=2

if pepperoni =='Y':
  if size=='M':
   price+=3
if pepperoni =='Y':
   if size=='L':
    price+=3
Extra_cheese = input("Do you want Extra Cheese? Yes or NO\n")
if Extra_cheese == 'Y':
   price+=1
print(f"your order is of {price}$")
