# 1. 13305 - 주유소 (https://www.acmicpc.net/problem/13305)
"""
문제 설명
어떤 나라에 N개의 도시가 있다. 이 도시들은 일직선 도로 위에 있다. 편의상 일직선을 수평 방향으로 두자.
제일 왼쪽의 도시에서 제일 오른쪽의 도시로 자동차를 이용하여 이동하려고 한다. 인접한 두 도시 사이의 도로들은 서로 길이가 다를 수 있다.
도로 길이의 단위는 km를 사용한다. 처음 출발할 때 자동차에는 기름이 없어서 주유소에서 기름을 넣고 출발하여야 한다.
기름통의 크기는 무제한이어서 얼마든지 많은 기름을 넣을 수 있다. 도로를 이용하여 이동할 때 1km마다 1리터의 기름을 사용한다.
각 도시에는 단 하나의 주유소가 있으며, 도시 마다 주유소의 리터당 가격은 다를 수 있다. 가격의 단위는 원을 사용한다.

각 도시에 있는 주유소의 기름 가격과, 각 도시를 연결하는 도로의 길이를 입력으로 받아
제일 왼쪽 도시에서 제일 오른쪽 도시로 이동하는 최소의 비용을 계산하는 프로그램을 작성하시오.
"""

# 내 풀이
import sys
input = sys.stdin.readline

n = int(input())
len = list(map(int, input().split()))
pri = list(map(int, input().split()))[:-1]

result = 0
for i in range(n - 1) :
    if i == 0 :
        result += pri[i] * len[i]
        pass
    else :
        if pri[i - 1] < pri[i] :
            pri[i] = pri[i - 1]
            result += pri[i] * len[i]
        else :
            result += pri[i] * len[i]
print(result)

# Case Study
import sys
r = sys.stdin.readline
N = int(r())

d = [int(i) for i in r().split()]
p = [int(i) for i in r().split()]

m = p[0]
ans = 0

for i in range(N - 1):
    m = min(m, p[i])
    ans += m * d[i]
print(ans)

"""
insight 정리
1. 내 풀이의 23 ~ 32줄, Case Study의 47 ~ 49 줄 비교하기.
2. 내 풀이를 기준으로
  -> 리스트 값을 굳이 업데이트 할 필요가 없었던 점
  -> 최솟값과 특정 값을 비교하는 방식이 비효율적이었던 점 체크
"""