import operator

#기차의 이름과 수송량이 담긴 튜플 리스트와 수송량의 합계를 기록할 딕셔너리 그리고 이를 다시 튜플 리스트로 바꿀 trainTup2 준비

trainTup1 = [('토마스', 5), ('헨리', 8), ('에드워드', 9), ('에밀리', 5), ('토마스', 4), ('헨리', 7),
         ('토마스', 3), ('에밀리', 8), ('퍼시', 5), ('고든', 13)]
trainDic, trainTup2 = {}, []
train = None
currentRank, totalRank = 1, 1

if __name__ == "__main__" :
    print("기차 수송량 목록 ==> ", trainTup1)
    print("-----------------------")

    #trainTup1을 딕셔너리로 변환, 딕셔너리의 키가 같으면 수송량 누적
    
    for train in trainTup1 :
        tname = train[0]
        tweight = train[1]
        if tname in trainDic :
            trainDic[tname] += tweight
        else :
            trainDic[tname] = tweight

#2019038030 김진영
            
    #기타 딕셔너리 값을 기준으로 정렬
            
    trainTup2 = sorted(trainDic.items(), key = operator.itemgetter(1), reverse = True)

    print("기차\t총 수송량\t순위")
    print("-----------------------")
    
    #첫번째 기차는 무조건 1등이므로 바로 출력
    
    print(trainTup2[0][0], '\t', trainTup2[0][1], '\t', currentRank)

    #두 번째 기차부터 출력, 전체 등수는 1씩 증가시키되 만약 앞 기차와 수송량이 같으면 currentRank 출력
    
    for i in range(1, len(trainTup2)) :
        totalRank += 1

        if trainTup2[i][1] == trainTup2[i-1][1] :
            pass
        else :
            currentRank = totalRank

        print(trainTup2[i][0], '\t', trainTup2[i][1], '\t', currentRank)
