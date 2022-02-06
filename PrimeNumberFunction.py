code for checking prime numbers:
def Prime_number(number):
  isprime=True
  for i in range(2,number):
   if number%i==0:
    isprime=False
  if isprime:
    print("This is a Prime number\n")

  else:
     print("This is not a prime number")




  
    

 
 
 

look = int(input("enter the number which you want to check\n"))

Prime_number(number=look)





