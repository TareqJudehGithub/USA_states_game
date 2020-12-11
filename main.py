import pandas
from turtle import Turtle, Screen

# Instances:
usa_map = Turtle()
screen = Screen()

# Screen setup:
screen.title("USA States Guessing Game")
screen.bgcolor("white")

# Setting up states map on screen:
image = "blank_states_img.gif"
screen.addshape(image)
usa_map.shape(image)

# Converting "state" column into a list:
states_data = pandas.read_csv("50_states.csv")
states_names = states_data["state"].to_list()

correct_answers = list()
game_on = True
while game_on:

    # User input:
    answer_state = screen.textinput(title=f"{len(correct_answers)}/50 States", prompt="Enter a state name: ", ).title()

    if answer_state == "exit".title():
        # Generating a new .csv file of states names we missed in order to learn:
        missing_states = list()
        for state in states_names:
            if state not in correct_answers:
                missing_states.append(state)

        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.scv")
        break

    if answer_state in states_names:
        sam = Turtle()
        sam.color("purple")
        sam.hideturtle()
        sam.penup()

        # go to state coordinates on map:
        answer_data = states_data[states_data["state"] == answer_state]
        sam.goto(int(answer_data["x"]), int(answer_data["y"]))
        sam.write(answer_state, align="center", font=("Arial", 9, "bold"))

        # Note: we could've also used pandas code in the .write() line above:
        # sam.write(answer_data["state"].item(), align="center", font=("Arial", 9, "normal"))
        correct_answers.append(answer_state)

    elif answer_state in correct_answers:
        print(f"{answer_state}")
        pass
    else:
        print("Wrong!")
        continue






