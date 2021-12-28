# 1. 11286 - 절댓값 힙 (https://www.acmicpc.net/problem/11286)
"""
문제 설명
절댓값 힙은 다음과 같은 연산을 지원하는 자료구조이다.

1. 배열에 정수 x (x ≠ 0)를 넣는다.
2. 배열에서 절댓값이 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다.
절댓값이 가장 작은 값이 여러개일 때는, 가장 작은 수를 출력하고, 그 값을 배열에서 제거한다.
프로그램은 처음에 비어있는 배열에서 시작하게 된다.

입력에서 0이 주어진 회수만큼 답을 출력한다.
만약 배열이 비어 있는 경우인데 절댓값이 가장 작은 값을 출력하라고 한 경우에는 0을 출력하면 된다.
"""

# 내 풀이
import sys
import heapq
from collections import deque

input = sys.stdin.readline
n = int(input())

heap = []
plus = []
minus = []

for _ in range(n) :
    num = int(input())
    if num == 0 :
        if len(heap) == 0 :
            print(0)
        else :
            num_2 = heapq.heappop(heap)
            if num_2 in minus :
                print(-1 * heapq.heappop(minus))
            else :
                print(heapq.heappop(plus))

    else :
        if num < 0 :
            heapq.heappush(minus, abs(num))
            heapq.heappush(heap, abs(num))
        else :
            heapq.heappush(plus, num)
            heapq.heappush(heap, num)

# Case Study
import sys
import heapq

numbers = int(input())
heap = []

for _ in range(numbers):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(heap, (abs(num), num))
    else:
        try:
            print(heapq.heappop(heap)[1])
        except:
            print(0)

"""
insight 정리
1. heap 자료 구조를 활용하여 양수 음수를 모두 포함하는 데이터를 관리할 때, 
tuple 형식으로 데이터를 입력함으로써 절댓값이 작은 순서대로 우선순위를 관리할 수 있음을 체크
"""

# ----------------------------------------------------------------------------

# 2. 1389 - 케빈 베이컨의 6단계 법칙 (https://www.acmicpc.net/problem/1389)
"""
문제 설명
케빈 베이컨의 6단계 법칙에 의하면 지구에 있는 모든 사람들은 최대 6단계 이내에서 서로 아는 사람으로 연결될 수 있다.
케빈 베이컨 게임은 임의의 두 사람이 최소 몇 단계 만에 이어질 수 있는지 계산하는 게임이다.

BOJ 유저의 수와 친구 관계가 입력으로 주어졌을 때, 케빈 베이컨의 수가 가장 작은 사람을 구하는 프로그램을 작성하시오.
"""

# 내 풀이
import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[sys.maxsize] * n for _ in range(n)]
for _ in range(m) :
    s, e = map(int, input().split())
    graph[s-1][e-1] = graph[e-1][s-1] = 1

for k in range(n) :
    graph[k][k] = 0
    for i in range(n) :
        for j in range(n) :
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

_sum = sys.maxsize
count = 0
for i in range(n) :
    li_sum = sum(graph[i])
    if li_sum < _sum :
        _sum = li_sum
        count = i + 1

print(count)

"""
insight 정리
1. 플로이드 와샬 유형의 전형적인 문제.
2. 개념 이해 참고 : https://brownbears.tistory.com/560
3. 처음 2중 리스트 잡을 때 sys.maxsize 설정하는 것, 3중 반복문에서 dp 개념이 활용되는 것 체크해두기
"""