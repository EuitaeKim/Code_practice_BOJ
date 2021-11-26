# 1. 1002 - 터렛 (https://www.acmicpc.net/problem/1002)
"""
문제 설명
조규현과 백승환은 터렛에 근무하는 직원이다. 하지만 워낙 존재감이 없어서 인구수는 차지하지 않는다. 다음은 조규현과 백승환의 사진이다.
이석원은 조규현과 백승환에게 상대편 마린(류재명)의 위치를 계산하라는 명령을 내렸다. 조규현과 백승환은 각각 자신의 터렛 위치에서 현재 적까지의 거리를 계산했다.
조규현의 좌표 (x1, y1)와 백승환의 좌표 (x2, y2)가 주어지고, 조규현이 계산한 류재명과의 거리 r1과 백승환이 계산한 류재명과의 거리 r2가 주어졌을 때,
류재명이 있을 수 있는 좌표의 수를 출력하는 프로그램을 작성하시오.
"""

# 내 풀이
import sys
n = int(sys.stdin.readline())

result = []
for _ in range(n) :
    x_1, y_1, r_1, x_2, y_2, r_2 = map(int, sys.stdin.readline().split())
    distance = ((x_1 - x_2) ** 2 + (y_1 - y_2) ** 2) ** 0.5
    if x_1 == x_2 and y_1 == y_2 and r_1 == r_2 :
        result.append(-1)
    elif r_1 + r_2 == distance or abs(r_1 - r_2) == distance :
        result.append(1)
    elif abs(r_1 - r_2) < distance < r_1 + r_2 :
        result.append(2)
    else :
        result.append(0)

for i in result :
    print(i)

"""
insight 정리
1. 수학 개념을 구현해야하는 문제를 풀 때, 답이 생각이 안난다면 코드 정답이 아닌 수학 개념을 알아보고 구현해볼 것
2. 두 점 사이의 distance와 r_1 & r_2의 관계를 조건절에서 비교할 때 조금의 오차로 인해 정상적인 판단을 못할수도 있다.
- https://mathbang.net/101 두 원의 위치관계에 대한 자료
- https://www.acmicpc.net/board/view/38854 해당 문제에서 주의해야 할 점
"""

# ----------------------------------------------------------------------------

# 2. 1463 - 1로 만들기 (https://www.acmicpc.net/problem/1463)
"""
문제 설명
정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지이다.
- X가 3으로 나누어 떨어지면, 3으로 나눈다.
- X가 2로 나누어 떨어지면, 2로 나눈다.
- 1을 뺀다.
정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.
"""

# 내 풀이
import sys
n = int(sys.stdin.readline())
result = []
count = 0
def calculate(num = n, count = count) :
    if num == 1 :
        return count
    elif num == 2 or num == 3 :
        return count + 1
    else :
        if num % 3 == 0 :
            count += 1
            return calculate(num // 3, count)
        if num % 2 == 0 :
            if (num - 1) % 3 == 0 : 
                count += 1
                return calculate(num - 1, count)
            else :
                count += 1
                return calculate(num // 2, count)
        else :
            count += 1
            return calculate(num - 1, count)

result.append(calculate(n, count))
print(min(result))

# Case Study
import sys

def calc(l) :
    global ans
    ans += 1
    nl = []
    for a in l :
        nl.append(a - 1)
        if a % 3 == 0 and a >= 3 :
            nl.append(a/3)
        if a % 2 == 0 and a >= 2 :
            nl.append(a/2)
    return nl

n = int(sys.stdin.readline())
l = []
l.append(n)
ans = 0
if n == 1 :
    print(ans)
else :
    while True :
        l = calc(l)
        print(l)
        if min(l) == 1 :
            break
    print(ans)

"""
insight 정리
1. 다이나믹 프로그래밍으로 문제를 해결하는 감은 있지만, 다양한 경우의 수를 고려한 후 최선의 답을 내는 알고리즘을 짜본적이 없어서 시간이 오래걸림
2. 내 코드의 64 ~ 70 줄을 보면 2로 나눌때 세부 조건을 추가한 부분이 있는데, 이렇게 일일히 세부 조건을 잡았더니 16에서 틀림(16 -> 15 -> 5 -> 4 -> 3 -> 1로 계산해버림. 정답은 16 -> 8 -> 4 -> 2 -> 1)
3. Case Study를 보면 주어진 수를 시작으로 함수를 적용할 때마다 주어진 3개의 경우의 수를 계속 적용하고 있으며, 한 사이클을 돌때 횟수를 count하고 있음. 그리고 어느 경우의 수든 최종 도출 값이 1이 나오면 break를 걸고 그때의 count 값을 도출함
"""