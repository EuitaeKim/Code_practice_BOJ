# 1. 11660 - 구간 합 구하기 5 (https://www.acmicpc.net/problem/11660)
"""
문제 설명
NxN개의 수가 NxN 크기의 표에 채워져 있다. (x1, y1)부터 (x2, y2)까지 합을 구하는 프로그램을 작성하시오.
"""

# 내 풀이
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
dp = []
for _ in range(n) :
    li = list(map(int, input().split()))
    for i in range(1, n) :
        li[i] += li[i-1]
    dp.append(li)

for _ in range(m) :
    a, b, c, d = map(int, input().split())
    a -= 1; b -= 1; c -= 1; d -= 1;
    result = 0
    for i in range(a, c+1) :
        if b == 0 or d == 0 :
            result += dp[i][d]
        else :
            result += (dp[i][d] - dp[i][b-1])
    
    print(result)

# Case Study
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
numbers = [[0]*(n+1)]

for _ in range(n):
    nums = [0]+[int(x) for x in input().split()]
    numbers.append(nums)

for i in range(1, n+1):
    for j in range(1, n):
        numbers[i][j+1] += numbers[i][j]

for j in range(1, n+1):
    for i in range(1, n):
        numbers[i+1][j] += numbers[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(numbers[x2][y2]-numbers[x1-1][y2]-numbers[x2][y1-1]+numbers[x1-1][y1-1])

"""
insight 정리
1. Case Study와 같은 dp기반의 해결 방법을 알아내긴 했으나, 예외 처리에 막혀서 한동안 해결하지 못헀었음
2. 구간이 왼쪽 혹은 위쪽으로 딱 붙어버릴 경우 인덱스가 음수가 나오기 때문에 이에 대한 예외를 하나하나 설정했었는데,
Case Study처럼 아얘 Pad Sequence를 잡아놓고 시작하면 특별한 예외처리를 하지 않아도 깔끔하게 답을 도출할 수 있음. 
"""