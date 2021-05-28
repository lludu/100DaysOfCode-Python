#This is day 6, Defining Funtions & While Loops & Karel

#Exercise 4 - Various Wall Heights & While loop:


def turn_right():
    turn_left()
    turn_left()
    turn_left()
while not at_goal():
    if right_is_clear():
       turn_right()
       move()
       turn_right()
       move()
    elif wall_in_front():
        turn_left()
    else:
        move()


#Angela's Longer Code
    def turn_right():
        turn_left()
        turn_left()
        turn_left()
    def jump():
        turn_left()
        while wall_on_right():
            move()
        turn_right()
        move()
        turn_right()
        while front_is_clear():
            move()
        turn_left()

    while not at_goal():
        if wall_in_front():
            jump()
        else:
            move()




#Link to Reeborg's World - Hurdle 4
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json
