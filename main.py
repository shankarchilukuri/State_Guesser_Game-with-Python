from turtle import Turtle,Screen
import pandas as p
s=Screen()
s.title("U.S States Game")
img="blank_states_img.gif"
s.addshape(img)

t=Turtle()
t.shape(img)
game_on=True
score =0
while score<50:
    te=s.textinput(title=f"{score}/{50} is correct",prompt="Whats another state name")
    text=te.title()
    data = p.read_csv("50_states.csv")
    correct = []
    if text=="Exit":
        l=[x for x in data.state if x not in correct]
        list=p.DataFrame(l)
        list.to_csv("States to Learn.csv")
        break


    for d in data.state:
        if d==text:
            correct.append(d)
            score+=1
            tim=Turtle()
            tim.penup()
            tim.hideturtle()
            da=(int(data.x[data.state==d]),int(data.y[data.state==d]))
            tim.goto(da)
            tim.write(d)





