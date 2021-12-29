# 1. 5525 - IOIOI (https://www.acmicpc.net/problem/5525)
"""
문제 설명
N+1개의 I와 N개의 O로 이루어져 있으면, I와 O이 교대로 나오는 문자열을 PN이라고 한다.
- P1 IOI
- P2 IOIOI
- PN IOIOI...OI (O가 N개)
I와 O로만 이루어진 문자열 S와 정수 N이 주어졌을 때,
S안에 PN이 몇 군데 포함되어 있는지 구하는 프로그램을 작성하시오.
"""

# 내 풀이
import sys
input = sys.stdin.readline
n = int(input()); m = int(input()); s = str(input().rstrip())

count = start = final = 0

while True :
    if start + 2 >= m :
        break
    if s[start : start + 2] == 'IO' :
        count += 1
        if count == n :
            if s[start + 2] == 'I' :
                final += 1
                count -= 1
            else :
                count = 0
        start += 2
    else :
        count = 0
        start += 1

print(final)

"""
insight 정리
1. k길이의 문자열을 직접 만들어 문자열의 0-k, 1-k+1, 2-k+2.. 범위를 각각 비교해도 되나, 이렇게하면 대략 O(m * k)의 시간복잡도를 갖게 된다.
2. 이를 효율적으로 탐색하기 위해 k길이 문자열의 최소 단위를 가져온 후 문자열 전체를 한번만 탐색함으로써 시간 효율적으로 처리할 수 있다.
"""

# ----------------------------------------------------------------------------

# 2. 6064 - 카잉 달력 (https://www.acmicpc.net/problem/6064)
"""
문제 설명
네 개의 정수 M, N, x와 y가 주어질 때,
<M:N>이 카잉 달력의 마지막 해라고 하면 <x:y>는 몇 번째 해를 나타내는지 구하는 프로그램을 작성하라.
"""

# 내 풀이
def num(m, n, x, y):
    while x <= m * n:
        if (x - y) % n == 0:
            return x
        x += m
    return -1

t = int(input())
for i in range(t):
    m, n, x, y = map(int, input().split())
    print(num(m, n, x, y))

"""
insight 정리
1. 중국인의 나머지 정리 관련 문제를 풀 때, 55번째 줄과 같은 세팅을 꼭 체크하기
"""