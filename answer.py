from turtle import Turtle


class Answer(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.state_x = 0
        self.state_y = 0

    def write_state(self, state, state_x, state_y):
        self.goto(state_x, state_y)
        self.write(state)
