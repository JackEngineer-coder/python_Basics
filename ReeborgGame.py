#Reeborg's world maze code:
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
    
while not at_goal():
    if front_is_clear() and right_is_clear():
        turn_right()
        move()                                
    elif  not front_is_clear() and right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
        
    
        
    elif wall_in_front() and right_is_clear():
         turn_right()
            
    elif wall_in_front():
         turn_left()
            
    
    
    #code2:
    def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
    
while front_is_clear():
      move()
turn_left()


while not at_goal():
    if right_is_clear():
       turn_right()
       move() 
        
    elif front_is_clear():
       move()
    else:
        turn_left()
        
    
    
