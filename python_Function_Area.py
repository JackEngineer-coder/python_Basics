#how much paint can you will need to paint a particular wall having some area:
def Can_need(width,height,coverage):
  need = (height*width)/coverage
  need_round = round(need)
  print(f"you will need {need_round} can")
h=int(input("enter the height of the wall\n"))
w=int(input("enter the width of the wall\n"))

Can_need(width=h,height=w,coverage=5)
