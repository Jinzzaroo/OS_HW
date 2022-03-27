import turtle
import math
import random

t = [None] * 3 #거북이 세 마리
t1X, t1Y, t2X, t2Y, t3X, t3Y = [0] * 6 #각 거북이의 위치 좌표
swidth, sheight = 1000, 600 #윈도창 크기
i = 0

if __name__ == "__main__" :
    turtle.title("거북이 만나기")
    #결과 화면(거북이 돌아다니는) 크기 설정
    turtle.setup(width = swidth + 50, height = sheight + 50)
    turtle.screensize(swidth, sheight)

    #각 거북이의 색 설정
    t[0] = turtle.Turtle('turtle'); t[0].color('red'); t[0].penup()
    t[1] = turtle.Turtle('turtle'); t[1].color('green'); t[1].penup()
    t[2] = turtle.Turtle('turtle'); t[2].color('blue'); t[2].penup()

    #각 거북이의 초기 위치 설정
    t[0].goto(-100, -100); t[1].goto(0, 0); t[2].goto(100, 100)
    t[0].speed(10); t[1].speed(10); t[2].speed(10)

##2019038030 김진영
    
    while True :
        #각 거북이에게 이동하는 명령어 추가
        for i in range (0, 3) :
            angle = random.randrange(0, 360)
            dist = random.randrange(1, 50)
            t[i].left(angle); t[i].forward(dist) #왼쪽으로 랜덤각 돈 후 앞으로 랜덤값 이동

        #각 거북이의 현재 위치 추출
        t1X = t[0].xcor(); t1Y = t[0].ycor()
        t2X = t[1].xcor(); t2Y = t[1].ycor()
        t3X = t[2].xcor(); t3Y = t[2].ycor()

        #거북이끼리 거리가 20 이하면 서로 만난 것으로 간주하고 크기가 세 배로 커진 후 종료
        if math.sqrt(((t1X -t2X) * (t1X - t2X)) + ((t1Y - t2Y) * (t1Y - t2Y))) <= 20 or \
           math.sqrt(((t1X -t3X) * (t1X - t3X)) + ((t1Y - t3Y) * (t1Y - t3Y))) <= 20 or \
           math.sqrt(((t2X -t3X) * (t2X - t3X)) + ((t2Y - t3Y) * (t2Y - t3Y))) <= 20 :
            t[0].turtlesize(3); t[1].turtlesize(3); t[2].turtlesize(3)
            break

    turtle.done()
