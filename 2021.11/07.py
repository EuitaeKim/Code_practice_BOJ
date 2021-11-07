# 1. 2309 - 일곱 난쟁이 (https://www.acmicpc.net/problem/2309)
"""
문제 설명
왕비를 피해 일곱 난쟁이들과 함께 평화롭게 생활하고 있던 백설공주에게 위기가 찾아왔다. 일과를 마치고 돌아온 난쟁이가 일곱 명이 아닌 아홉 명이었던 것이다.
아홉 명의 난쟁이는 모두 자신이 "백설 공주와 일곱 난쟁이"의 주인공이라고 주장했다. 뛰어난 수학적 직관력을 가지고 있던 백설공주는, 다행스럽게도 일곱 난쟁이의 키의 합이 100이 됨을 기억해 냈다.
아홉 난쟁이의 키가 주어졌을 때, 백설공주를 도와 일곱 난쟁이를 찾는 프로그램을 작성하시오.
"""

# 내 풀이
import sys
li = [int(sys.stdin.readline()) for _ in range(9)]
li.sort()

result_1 = []
for i in range(0, 3) :
    if sum(li[0+i:7+i]) == 100 :
        result_1.append(li[0+i:7+i])

if len(result_1) != 0 :
    for i in result_1[0] :
        print(i)
else :
    result_2 = []
    for i in [7, 8] :
        for j in range(0, 7) :
            li_2 = li.copy()
            li_2[j] = li_2[i]
            li_2 = li_2[0:7]
            li_2.sort()
            if sum(li_2[0:7]) == 100 :
                result_2.append(li_2[0:7])
    if len(result_2) != 0 :
        for i in result_2[0] :
            print(i)
    else :
        result_3 = []
        for i in range(0, 7) :
            for j in range(i, 7) :
                li_3 = li.copy()
                li_3[i], li_3[j] = li_3[7], li_3[8]
                li_3 = li_3[0:7]
                li_3.sort()
                if sum(li_3[0:7]) == 100 :
                    result_3.append(li_3[0:7])
        if len(result_3) != 0 :
            for i in result_3[0] :
                print(i)

# Case Study
import random
heights = [int(input()) for i in range(9)]

while True:
    sampleList = random.sample(heights, 7)
    sampleList.sort()
    if sum(sampleList)==100:
        for sample in sampleList:
            print(sample)
        break

"""
insight 정리
1. 정말 하나하나 다 구할 것인지.. 랜덤 함수써서 답이 나올때까지 구할 것인지..
하나하나 다 구한 내 방법이 시간으로는 효율적이었지만, 코드가 너무너무 복잡해지기 때문에 이럴 바에는 random을 쓰는게 맘이 편한 것 같다.
"""