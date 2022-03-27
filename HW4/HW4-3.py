import turtle
import random

myTurtle, tX, tY, tColor, tSize, tAngle = [None] * 6
playerTurtles = []
swidth, sheight = 500, 500

if __name__ == "__main__" :
    
    #프로그램 실행 창 설정
    
    turtle.title('거북이 리스트 활용(정렬)')
    turtle.setup(width = swidth + 50, height = sheight + 50)
    turtle.screensize(swidth, sheight)

    #5개의 터틀들이 포함된 2차원 리스트 만들기
    
    for i in range(0, 5) :

        #터틀의 (모양, 위치, 색, 사이즈, 각도) 변수 초기화
        
        myTurtle = turtle.Turtle("turtle")
        tX = random.randrange( -250, 250)
        tY = random.randrange( -250, 250)
        r = random.random(); g = random.random(); b = random.random()
        tSize = random.randrange(10,100)/10
        tAngle = random.randrange(0, 361)

        #생성되는 터틀들의 2차원 리스트 설정
        
        playerTurtles.append([myTurtle, tX, tY, tSize, tAngle, r, g, b])

#2019038030 김진영

    #playerTurtles 리스트 속 터틀들에게 값을 초기화 (penup한 상태)
        
    for tList in playerTurtles :
        myTurtle = tList[0]
        myTurtle.color(tList[5], tList[6], tList[7])
        myTurtle.turtlesize(tList[3])
        myTurtle.penup()
        myTurtle.speed(6)
        myTurtle.goto(tList[1], tList[2])
        myTurtle.right(tList[4])

    #playerTurtles 리스트를 key = 터틀 사이즈(tList[3]) 로 놓고 정렬
        
    sortedTurtles = sorted(playerTurtles, key = lambda tList : tList[3])

    #터틀들간에 선 그리기
    #새로운 터틀을 만들어서 터틀 모양을 숨기고 정렬된 첫번째 터틀의 좌표로 이동
    #pendown하고 그 다음 터틀 좌표로 이동
    
    for i in range(0, 5) :
        turtle.hideturtle()
        turtle.penup()
        turtle.speed(10)
        turtle.goto(sortedTurtles[i][1], sortedTurtles[i][2])
        turtle.pencolor(sortedTurtles[i][5], sortedTurtles[i][6], sortedTurtles[i][7])
        turtle.pendown() 
        if i < 4 : #over index 방지
            turtle.goto(sortedTurtles[i+1][1], sortedTurtles[i+1][2])
        else :
            break
        

    
    

        
        
        
        
        
