import turtle
import pandas

screen=turtle.Screen()
screen.title("US States Game")
image="blank_states_img.gif"
guessed=[]
missed=[]
screen.addshape(image)
data=pandas.read_csv("50_states.csv")
data_states=data.state.to_list()
turtle.shape(image)
while len(guessed)<50:
    if len(guessed)<1:
         answer_state=screen.textinput(title="Guess the State",prompt="What's another states name?").title()
    else:
        answer_state = screen.textinput(title=f"{len(guessed)}/50 States", prompt="What's another states name?").title()
    if answer_state == "Exit":
        for i in data_states:
            if i not in guessed:
                missed.append(i)
        new_data=pandas.DataFrame(missed)
        new_data.to_csv("To Learn")

        break


    if answer_state in data_states:
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data.state==answer_state]
        t.goto(state_data.x.item(),state_data.y.item())
        t.write(answer_state)
        guessed.append(answer_state)




turtle.mainloop()