#Code for adding numbers
total=0
count=0
for number in range(2,102,2):
 
 total+=number

 print(number)
print(total)



#fizz-buzz code:
for number in range(1,101):
  if number%3==0 and number%5==0:
   number="fizz-buzz"
  elif number%3==0:
    number="fizz"
  elif number%5==0:
    number="buzz"
  print(number)
