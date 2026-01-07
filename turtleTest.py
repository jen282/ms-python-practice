import turtle as t
import random 

turtle_list = []
turtle_color = ['red', 'green', 'violet', 'blue']

def createTurtle(num):
    for i in range(num):
        newTurtle = t.Turtle()
        newTurtle.shape('turtle')
        newTurtle.color(turtle_color[random.randint(0,3)])
        turtle_list.append(newTurtle)
       
def drawReg(t, x, y, wid, hei):
    t.penup()
    t.goto(x, y)
    t.pendown()
    for i in range(2):
        t.forward(wid)
        t.right(90)
        t.forward(hei)
        t.right(90)

if __name__ == "__main__":
    t_num = int(input('생성할 거북이 개수를 입력하세요'))
    createTurtle(t_num)
    for i in range(t_num):
        drawReg(turtle_list[i], 
                    -200 + i*100, -100 + i*50,
                    60, 40)
          
    