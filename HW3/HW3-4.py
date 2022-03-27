import turtle

#중첩 반복문을 위한 i, k / 거북이 좌표 tX, tY / 결과창 크기 swidth, sheight
i, k, tX, tY = [0] * 4
swidth, sheight = 800, 450

if __name__ == "__main__" :
    turtle.title('거북 구구단')
    turtle.shape('turtle')
    turtle.setup(width = swidth + 50, height = sheight + 50)
    turtle.screensize(swidth, sheight)
    turtle.penup() #거북이 이동하면서 선 x
    
    #거북이 초기위치 설정
    tX, tY = -500, 250
    turtle.goto(tX, tY)

##2019038030 김진영

    for i in range(1,10) :          # 곱하기 1, 곱하기 2, 곱하기 3 ... 반복(행)
        for k in range(2, 10) :     #2단, 3단 4단 ... 반복(열)
            turtle.goto(tX + 80*k, tY - 40*i) #출력하려는 위치로 이동
            gugu = str(k) + 'x' + str(i) + '=' + str(k*i) #식 출력
            turtle.write(gugu, font = ('Arial', 12, 'bold')) #식 글씨체

    turtle.done()
