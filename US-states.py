import turtle
import pandas

screen = turtle.Screen()
screen.title('US States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('50_states.csv')
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    user_input = screen.textinput(title=f'{len(guessed_states)}/50 checked states',
                                  prompt="What's the next state?").title()

    if user_input == 'Exit':
        missing_states = [state for state in all_states if state not in guessed_states]
        print(missing_states)
        break

    if user_input in all_states:
        guessed_states.append(user_input)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_data = data[data.state == user_input]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(user_input)

new_data = pandas.DataFrame(missing_states)
new_data.to_csv('states_to_learn.csv')