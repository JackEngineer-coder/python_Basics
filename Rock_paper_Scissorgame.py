# Treasure game

row1 = ["🥲","🥲","🥲"]
row2 = ["🥲","🥲","🥲"]
row3 = ["🥲","🥲","🥲"]
map=[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
location=input("Enter the treasure location")

horizontal = int(location[0])
vertical = int(location[1])

map[horizontal-1][vertical-1]="X"
print(f"{row1}\n{row2}\n{row3}")








Rock paper Scicor game
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


import random
user_inp=int(input("Enter 0 for rock, enter 1 for paper and enter 2 for scissors\n"))
if user_inp<0 or user_inp>2:
  print("Invalid entry, you loose")
else:
 game_image = [rock,paper,scissors]
 print(game_image[user_inp])
 computer_inp = random.randint(1,2)
 print("Computer choose:")
 print(game_image[computer_inp])





 if user_inp>computer_inp:
  print("you won")

 elif user_inp==0 and computer_inp==2:
  print("you won")

 elif computer_inp>user_inp:
  print("you loose")

 elif computer_inp==0 and user_inp==2:
  print("you loose")

 elif user_inp==computer_inp:
  print("It is draw")





    
