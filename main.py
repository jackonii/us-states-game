import turtle
import pandas as pd  # pip install pandas
import csv

FONT = ("Arial", 8, "normal")

screen = turtle.Screen()
image = "blank_states_img.gif"
screen.bgpic(image)
screen.title("U.S. States Game")

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()


quiz_data = pd.read_csv("50_states.csv")
us_states = list(quiz_data['state'])

title = "Guess the State"
is_on = True

while is_on:
    answer_state = screen.textinput(title=title, prompt="What's another state's name?").title()
    if answer_state == "Exit":
        break
    if answer_state in us_states:
        state_x = int(quiz_data[quiz_data['state'] == f'{answer_state}']['x'])
        state_y = int(quiz_data[quiz_data['state'] == f'{answer_state}']['y'])
        pen.goto(state_x, state_y)
        pen.write(f"{answer_state}", align="center", font=FONT)
        us_states.remove(answer_state)
        title = f"{50-len(us_states)}/50 States Correct"
        if len(us_states) == 0:
            is_on = False


states_to_learn = pd.DataFrame({'states': us_states})
states_to_learn.to_csv("states_to_learn.csv")

