# 1. 1929 - 소수 구하기 (https://www.acmicpc.net/problem/1929)
"""
문제 설명
M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.
"""

# 내 풀이
import sys
t, p = map(int, sys.stdin.readline().split())

stan = int(p**0.5)

result = []
for i in range(t, p+1) :
    log = []
    for j in range(2, stan + 1) :
        if i > j :
            if i % j != 0 :
                log.append('t')
            else :
                log.append('f')

    if 'f' not in log :
        result.append(i)

for i in result :
    print(i)

# Case Study
import sys
t, p = map(int, sys.stdin.readline().split())

li = [0 for _ in range(p+1)]

for i in range(2, p+1) :
    if li[i] == 0 :
        for j in range(i, p+1, i) :
            li[j] = 1
        li[i] = 2

for i in range(t, p+1) :
    if li[i] == 2 :
        print(i)

"""
insight 정리
1. 에라토스테네스의 체를 적은 비용으로 구현하려고 변형했다가 오히려 시간초과 난 케이스 -> 리스트 2개 생성 및 불필요한 연산 때문에 시간초과가 난 것으로 추측 됨
2. 에라토스테네스의 체 원리를 최대한 그대로 구현하는 것을 먼저하고, 시간초과가 날 경우 다른 케이스를 고민할 것
"""

# ----------------------------------------------------------------------------

# 2. 18111 - 마인크래프트 (https://www.acmicpc.net/problem/18111)
"""
문제 설명
팀 레드시프트는 대회 준비를 하다가 지루해져서 샌드박스 게임인 ‘마인크래프트’를 켰다.
마인크래프트는 1 × 1 × 1(세로, 가로, 높이) 크기의 블록들로 이루어진 3차원 세계에서 자유롭게 땅을 파거나 집을 지을 수 있는 게임이다.
목재를 충분히 모은 lvalue는 집을 짓기로 하였다.
하지만 고르지 않은 땅에는 집을 지을 수 없기 때문에 땅의 높이를 모두 동일하게 만드는 ‘땅 고르기’ 작업을 해야 한다.
lvalue는 세로 N, 가로 M 크기의 집터를 골랐다. 집터 맨 왼쪽 위의 좌표는 (0, 0)이다. 우리의 목적은 이 집터 내의 땅의 높이를 일정하게 바꾸는 것이다. 우리는 다음과 같은 두 종류의 작업을 할 수 있다.
1. 좌표 (i, j)의 가장 위에 있는 블록을 제거하여 인벤토리에 넣는다.
2. 인벤토리에서 블록 하나를 꺼내어 좌표 (i, j)의 가장 위에 있는 블록 위에 놓는다.
1번 작업은 2초가 걸리며, 2번 작업은 1초가 걸린다. 밤에는 무서운 몬스터들이 나오기 때문에 최대한 빨리 땅 고르기 작업을 마쳐야 한다.
‘땅 고르기’ 작업에 걸리는 최소 시간과 그 경우 땅의 높이를 출력하시오.
"""

# 내 풀이
import sys
from collections import Counter

n, m, b = map(int, sys.stdin.readline().split())

li = []
for _ in range(n) :
    for i in list(map(int, sys.stdin.readline().split())) :
        li.append(i)

li = dict(Counter(li))
li_2 = [[k, v] for k, v in sorted(li.items(), reverse=True)]

def floorup(time, up, b, list) :
    time += up
    b -= up
    if list[-1][0] + 1 == list[-2][0] :
        list[-2][1] += list[-1][1]
        list.pop()
    else :
        list[-1][0] += 1
    return time, b, list

def floordown(time, down, b, list) :
    time += down
    b += down//2
    if list[0][0] -1 == list[1][0] :
        list[1][1] += list[0][1]
        list.pop(0)
    else :
        list[0][0] -= 1
    return time, b, list

down = (li_2[0][1]) * 2
up = (li_2[-1][1])
time = 0

while len(li_2) > 1 :
    if down >= up :
        if (b-up) >= 0 :
            time, b, li_2 = floorup(time, up, b, li_2)
        else :
            time, b, li_2 = floordown(time, down, b, li_2)
    else :
        time, b, li_2 = floordown(time, down, b, li_2)

print(f"{time} {max(li_2[0])}")

# Case Study
import sys
input = sys.stdin.readline

n,m,b = map(int,input().split())
g = []
for _ in range(n):
    g.append(list(map(int,input().split())))

Min = min(map(min,g))
Max = max(map(max,g))
least = 1e9

for i in range(Min, Max+1):
    plu = 0
    min = 0
    for j in range(n):
        for k in range(m):
            h = g[j][k] - i
            if h>0:
                min += h
            elif h<0:
                plu -= h
    if min+b>=plu:
        time = min*2 + plu
        if least >= time:
            least = time
            H = i
            
print(least,H)

"""
insight 정리
1. 브루트 포스 알고리즘의 정확한 접근 방법을 모르고 냅다 들이댔더니 알고리즘의 끝을 봐버렸다. 정말 이렇게 하나하나 다 구하는 무식한 알고리즘이구나라고 뼈저리게 느꼈다.
2. 때문에 앞으로 브루트 포스 알고리즘 문제를 보면, 주어진 변수의 Limit를 가장 먼저 확인할 것이다. 그리고 1부터 Limit까지 모든 경우를 구하는 것을 Default로 머릿속에 새길 것이다.
3. 괜히 효율적으로 하겠다고 주어진 변수를 안 쓰고 자료구조를 막 갖다 썼는데, 변수를 주는 데는 이유가 있는거 같다. 이번 기회에 딕셔너리에 대해 정말 많은 걸 배웠지만, 주는 대로만 하자.
4. 이번에 PyPy3를 처음 써봤다. PyPy는 Python3의 실행시 시간이 매우 오래 걸린다는 단점을 개선하고자 JIT컴파일 방식을 도입한 것이라고 한다.
자세한 내용 참조 : https://ralp0217.tistory.com/entry/Python3-와-PyPy3-차이
"""

# ----------------------------------------------------------------------------