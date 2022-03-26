import turtle

##전역 변수 부분##
num = 0
swidth, sheight = 1000, 300
curX, curY = 0,0

##메인 코드 부분##
if __name__ == "__main__" :
    turtle.title('거북이로 2진수 표현하기')
    turtle.shape('turtle')
    turtle.setup(width = swidth + 50, height = sheight + 50)    ## 그래픽 창 크기 설정
    turtle.screensize(swidth, sheight)                          ##배경 크기 설정
    turtle.penup()
    turtle.left(90)      ##거북이가 위로보게끔

    num = int(input("숫자를 입력하세요 : "))
    binary = bin(num)    ##입력받은 십진수를 이진수를 변환(ex. 9 -> 0b1001)
    curX = swidth/2
    curY = 0

##2019038030 김진영
    
    for i in range(len(binary)-2) : ##이진수 앞부분 0b를 제외한 길이값만큼 반복
        turtle.goto(curX, curY)

        if num&1:                   ##num을 이진수로 변환하여 <맨 하위 비트 == 1>
            turtle.color('red')
            turtle.turtlesize(2)

        else:
            turtle.color('blue')
            turtle.turtlesize(1)

        turtle.stamp()
        curX -= 50
        num >>= 1                   ##num을 이진수로 변환하여 <오른쪽으로 1 시프트> 후 그 값을 다시 십진수로

turtle.done()


