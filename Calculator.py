from replit import clear 
def add(n1,n2):
  result = n1+n2
  return result

def subtract(n1,n2):
  result = n1-n2
  return result

def multiply(n1,n2):
  result = n1*n2
  return result

def divide(n1,n2):
  result = n1/n2
  return result

def keywords():
  print("+\n-\n*\n/\n")




n1=float(input("enter your 1st number\n"))

continue_ = True
while continue_:

  keywords()
  key= input("Enter your desired operation  ")

  n2=float(input("enter your other number"))
  

  if key=="+":
    a=float((add(n1,n2)))
    print(a)

  elif key=="-":
    a=float(subtract(n1,n2))
    print(a)
  elif key=="*":
    a=(multiply(n1,n2))
    print(a)
  elif key=="/":
    a=(divide(n1,n2))
    print(a)

  should_continue= input("want to continue the operations yes or No?")

  if should_continue=="y":
    n1=a
  else:
    continue_=False
    clear()





