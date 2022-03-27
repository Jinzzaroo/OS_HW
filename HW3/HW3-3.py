h = "" #수 문자열
i = 0  #반복문을 위한 변수

if __name__ == "__main__" :
    #h에 수 문자열 입력
    h = input("숫자를 여러 개 입력하세요 : " )
    print("")

##2019038030 김진영
    
    for i in range (0, len(h)) :        #문자열 길이만큼 반복(12345면 5번 반복)
        for i in range(0, int(h[i])) :  #문자열의 각 수의 값만큼 반복
            print("\u2665", end = "")   #하트 한 줄로 출력
        print("")
