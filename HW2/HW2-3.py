##변수 선언 부분##
inStr = ''

##메인 코드 부분##
if __name__ == "__main__":
    inStr = input('문자열을 입력 -->')

##2019038030 김진영
    
    for i in range(len(inStr)-1,-1,-1):
        print('%c' %inStr[i], end='')

## 만약 inStr = 'hello' 라면 len(inStr) = 5
## range(len(inStr)-1,-1,-1) = len(inStr)-1, len(inStr)-2, ... , 3, 2, 1, 0
## end = '' 는 한 줄에 써지도록 하는 것
