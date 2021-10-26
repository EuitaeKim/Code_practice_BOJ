# 1. 1874 - 스택 수열 (https://www.acmicpc.net/problem/1874)
"""
문제 설명
스택 (stack)은 기본적인 자료구조 중 하나로, 컴퓨터 프로그램을 작성할 때 자주 이용되는 개념이다.
스택은 자료를 넣는 (push) 입구와 자료를 뽑는 (pop) 입구가 같아 제일 나중에 들어간 자료가 제일 먼저 나오는 (LIFO, Last in First out) 특성을 가지고 있다.
1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써, 하나의 수열을 만들 수 있다.
이때, 스택에 push하는 순서는 반드시 오름차순을 지키도록 한다고 하자.
임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지, 있다면 어떤 순서로 push와 pop 연산을 수행해야 하는지를 알아낼 수 있다. 이를 계산하는 프로그램을 작성하라.
"""

# 내 풀이
import sys

n = int(sys.stdin.readline())
li = [int(sys.stdin.readline()) for _ in range(n)]

com = [i for i in range(0, n+1)]
start = 0
stack = []
a = ''
for i in li :
    while True :
        try :
            if i > com[start] :
                start += 1
                stack.append('+')
            elif i < com[start] :
                com.pop(start)
                stack.append('-')
            else :
                com.pop(start)
                start -= 1
                stack.append('-')        
                break
        except :
            a = 'error'
            break

if a == 'error' :
    print('NO')
else :
    for i in stack :
        print(i)

# Case Study
from sys import stdin

cycle = int(stdin.readline())

stack = []
answer = []
cur = 1
status = 1

for _ in range(cycle):
    n = int(stdin.readline())
    while cur <= n:
        stack.append(cur)
        answer.append('+')
        cur += 1

    if stack[-1] == n:
        stack.pop()
        answer.append('-')
    else:
        status = 0
        print('NO')
        break
        
if status == 1:
    for i in answer:
        print(i)

"""
insight 정리
1. 메모리: 38216KB, 시간: 2040ms -> 메모리: 31296KB, 시간: 220ms
2. 헷갈렸던 부분 - 여기서의 pop 연산은 값을 버리는 게 아니고 정답 리스트에 넣는다는 것을 의미함. 때문에 62~68줄처럼 단순 연산을 통한 계산이 가능했던 것
3. 내 코드도 한 번에 통과하긴 했지만, 문제의 조건을 디테일하게 보면서 효율적인 계산을 고려할 것. 이런 생각 안하면 앞으로 쭉~~ 아래 문제처럼 완전 헛짓거리 할 듯 ^^
"""

# ----------------------------------------------------------------------------


# 2. 1966 - 프린터 큐 (https://www.acmicpc.net/problem/1966)
"""
문제 설명
여러분도 알다시피 여러분의 프린터 기기는 여러분이 인쇄하고자 하는 문서를 인쇄 명령을 받은 ‘순서대로’, 즉 먼저 요청된 것을 먼저 인쇄한다.
여러 개의 문서가 쌓인다면 Queue 자료구조에 쌓여서 FIFO - First In First Out - 에 따라 인쇄가 되게 된다.
하지만 상근이는 새로운 프린터기 내부 소프트웨어를 개발하였는데, 이 프린터기는 다음과 같은 조건에 따라 인쇄를 하게 된다.

현재 Queue의 가장 앞에 있는 문서의 ‘중요도’를 확인한다.
나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 한다. 그렇지 않다면 바로 인쇄를 한다.
예를 들어 Queue에 4개의 문서(A B C D)가 있고, 중요도가 2 1 4 3 라면 C를 인쇄하고, 다음으로 D를 인쇄하고 A, B를 인쇄하게 된다.

여러분이 할 일은, 현재 Queue에 있는 문서의 수와 중요도가 주어졌을 때, 어떤 한 문서가 몇 번째로 인쇄되는지 알아내는 것이다.
예를 들어 위의 예에서 C문서는 1번째로, A문서는 3번째로 인쇄되게 된다.
"""

# 내 풀이
import sys
r = int(sys.stdin.readline())

for _ in range(r) :
    c, l = map(int, sys.stdin.readline().split())
    li = list(map(int, sys.stdin.readline().split()))
    idx = l
    count = 1

    while True :
        if len(li) == 1 :
            print(count)
            break
        
        if li[0] < max(li[1:]) :
            li.append(li.pop(0))
            idx = len(li) - 1
        elif (li[0] >= max(li[1:])) and (idx != l) :
            li.pop(0)
            idx -= 1
            if idx == 0:
                print(count)
                break
            else :
                count += 1

# Case Study
test_cases = int(input())

for _ in range(test_cases):
    n, m = list(map(int, input().split()))
    imp = list(map(int, input().split()))
    idx = list(range(len(imp)))
    idx[m] = 'target'

    order = 0
    
    while True:
        if imp[0]==max(imp):
            order += 1
            if idx[0]=='target':
                print(order)
                break
            else:
                imp.pop(0)
                idx.pop(0)
        else:
            imp.append(imp.pop(0))
            idx.append(idx.pop(0))

"""
insight 정리
1. 시간, 메모리 제한에 쫄아 새로운 리스트 생성 및 활용을 생각도 하지 않은 것이 큰 문제.
2. Case Study의 핵심은 인덱스 리스트를 추가로 만들고, 내가 찾고자 하는 인덱스 값을 'target'으로 대체해버린 것
-> 이 방법이 나한테 너무 생소해서 구현을 생각하지도 못함. 앞으로 유사한 문제 풀 때 참고할 것
"""