import operator

trainTup1 = [('토마스', 5), ('헨리', 8), ('에드워드', 9), ('에밀리', 5), ('토마스', 4), ('헨리', 7),
         ('토마스', 3), ('에밀리', 8), ('퍼시', 5), ('고든', 13)]
trainDic, trainTup2 = {}, []
train = None
tname, tweight, rank = "", 0, 0

if __name__ == "__main__" :
    print("기차 수송량 목록 ==> ", trainTup1)
    

    for train in trainTup1 :
        tname = trainTup1[0]
        tweight = trainTup1[1]

    if tname in trainTup1 :
        trainTup2[tname] += tweight

    trainDic = dict(trainTup2)

    print("기차 수송량 목록 ==> ", trainDic)

    print("-----------------------")
    print("기차     총수송량   순위")
