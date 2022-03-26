import turtle
import random

## 함수 선언 부분 ##
def  screenRightClick(x, y):

    tSize = random.randrange(1, 10) 
    turtle.shapesize(tSize)

    global r, g, b
    r = random.random()
    g = random.random()
    b = random.random()

    turtle.pencolor((r, g, b))
    turtle.color((r, g, b))

    turtle.pendown()
    turtle.goto(x, y)

    turtle.stamp()

##2019038030 김진영##

    
## 변수 선언 부분 ##
pSize = 5
r, g, b = 0.0, 0.0, 0.0

## 메인 코드 부분 ##
turtle.title('거북이로 그림 그리기')
turtle.shape('turtle')
turtle.pensize(pSize)

turtle.onscreenclick(screenRightClick, 3)


turtle.done()
