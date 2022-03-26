import random

data = []
i, k = 0, 0

if __name__ == "__main__" :

    #10개의 16진수를 랜덤으로 생성하여 리스트
    
    for i in range (0, 10) :
        data.append(hex(random.randrange(0, 10000)))

    print("정렬 전 데이터 : ", end = '')
    for i in range(0, 10) :
        print(data[i]," ", end = '')

    print("\n정렬 후 데이터 : ", end ='')

##2019038030 김진영
    
    #index i번째 수가 index i+1 ~ 9번째 수보다 크면 swap
    for i in range (0, 10) :
        for k in range (i+1, 10) :
            if data[i] > data[k] :
                tmp = data[i]
                data[i] = data[k]
                data[k] = tmp
                
    for i in range (0, 10) :
        print(data[i]," ", end = '')
