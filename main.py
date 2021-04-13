import turtle
import pandas
from answer import Answer

from scoreboard import Scoreboard

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

scoreboard = Scoreboard()

data = pandas.read_csv("50_states.csv")
correct_list = []
game_is_on = True
while game_is_on:
    user_answer = screen.textinput(title=f"{scoreboard.score}/50 States Correct", prompt="What's another state name?").title()

    if user_answer == "Exit":
        break
    if user_answer in data.values:
        new_turtle = Answer()
        correct_list.append(new_turtle)

        state_x = int(data[data.state == user_answer].x)
        state_y = int(data[data.state == user_answer].y)
        print(f"coord: {state_x}, {state_y}")
        new_turtle.write_state(user_answer, state_x, state_y)

        scoreboard.increase_score()

    else:
        print("Cueck")
