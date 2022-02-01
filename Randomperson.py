#code for selecting random person's name from the list
import random
str_inp =input("Give me eveybodies name, seperated by a comma.\n")
names =str_inp.split(",")
Total_name =len(names)
Choices= random.randint(0,Total_name - 1)
Random_person= names[Choices]
print(Random_person)





