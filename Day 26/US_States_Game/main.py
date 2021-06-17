import turtle
import pandas
# # # https://pandas.pydata.org/docs/user_guide/index.html # # #

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
screen.setup(width=800, height=550)
turtle.shape(image) # make a blank turtle the map image as a shape


# # # --------------- GET COORDINATES IN TURTLE BY CLICKING IN TURTLE WINDOW --------------- # # #
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()  # Keeps Screen Open


# # # ---- Set variables ---- # # #
# score = 0
game_title = "Guess a State"
# state_names_stripped = []
guessed_states = []
game_is_on = True

# # # --- Set writing turtle --- # # #
writer = turtle.Turtle()
writer.penup()
writer.shape("classic")
writer.speed(10)
writer.hideturtle()

title_turt = turtle.Turtle()
title_turt.penup()
title_turt.shape("classic")
title_turt.speed(10)
title_turt.hideturtle()

# # # --------------- Import CSV Data for Map ------------- # # #
data = pandas.read_csv("50_states.csv")
state_names = list(data.state) # convert state names series into a list


# # # ------- If stripping white space out, the game is fixed so this shouldnt be nescessary ---- # # #
# for state in state_names:
#     string = state
#     stripped_state = string.replace(' ','')
#     state_names_stripped.append(stripped_state)


title_turt.goto(0, 250)
title_turt.write("Guess all the states, type 'exit' to quit.", align="Center")
while game_is_on:



    answer_state = screen.textinput(title=game_title, prompt="What's a state's name?").title()  # Prompt the user for a state
    # stripped_answer = answer_state.replace(' ','')  # --- shouldnt need this


    if answer_state in state_names:
    # if stripped_answer in state_names_stripped: # --- shouldnt need this
        state_data = data[data.state == answer_state]  # store the row that contains the state the user answered correctly
        writer.goto(int(state_data.x), int(state_data.y)) # tell the writer to go to the state's coords
        writer.write(answer_state) # Write the state name
        # score += 1 # add a point if they got the state
        guessed_states.append(answer_state)
        # game_title = f"{score}/50 States Correct" # change title bar for prompt window
        game_title = f"{len(guessed_states)}/50 States Correct" # change title bar for prompt window
        title_turt.clear()
        title_turt.goto(0, 250)
        title_turt.write(f"{len(guessed_states)}/50 States Correct, type 'exit' to quit.", align="Center")

    if answer_state == "Exit":
        # new_list = [new_item for item in item if test]
        missing_states = [state for state in state_names if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        game_is_on = False
        break

    if len(guessed_states) == 50:
    # if score == 50:
        title_turt.clear()
        title_turt.goto(0, 250)
        title_turt.write("CONGRATS YOU GOT THEM ALL", align="Center")
        game_is_on = False
        screen.exitonclick()


