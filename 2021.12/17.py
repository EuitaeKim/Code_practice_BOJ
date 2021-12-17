# 1. 1699 - 제곱수의 합 (https://www.acmicpc.net/problem/1699)
"""
문제 설명
주어진 자연수 N을 이렇게 제곱수들의 합으로 표현할 때에 그 항의 최소개수를 구하는 프로그램을 작성하시오.
"""

# 내 풀이
import sys
n = int(sys.stdin.readline())
dp = [n]
count = 0

while True :
    li = []
    count += 1

    for j in dp :
        for i in range(int(j ** 0.5), 0, -1) :
            if j - (i ** 2) >= 0 : 
                li.append(j - (i ** 2))
        
    if 0 in li :
        break
    else :
        dp = li

print(count)

# Case Study
import sys
n = int(sys.stdin.readline())
dp = [i for i in range(n + 1)]

for i in range(1, n + 1) :
    for j in range(1, i) :
        if j * j > i :
            break

        if dp[i] > dp[i - j * j] + 1 :
            dp[i] = dp[i - j * j] + 1

print(dp[n])

"""
insight 정리
1. 이전과 같은 전형적인 dp 문제이지만, 체감 난이도가 너무 높았던 문제.
2. 이번 문제는 하나의 결과 값을 얻기 위해 다양한 경우의 수를 비교해야 했다.
3. 2를 위해 나는 n이 취할 수 있는 모든 제곱 수를 계산. 그리고 결과 값이 0이 나올 때 break 후 count 값을 반환. 그러나 시간 초과 및 메모리 초과 모두 걸림
4. Case Study의 경우 주어진 n이 취할 수 있는 모든 제곱 수와 n - 1까지의 값은 최솟값 임이 보장되는 원리를 이용하여 답을 도출 함
5. 내 풀이 예) n = 12일 경우, 12 -> 11, 8, 3 -> 10, 7, 3, 4, 2 -> 9, 6, 1, 3, 2, 0, 1 -> 답 3
6. Case Study 예) n = 12일 경우, li[12] = min(li[11] + 1, li[8] + 1, li[3] + 1) -> 답 3
"""

# ----------------------------------------------------------------------------

# 2. 15650 - N과 M(2) (https://www.acmicpc.net/problem/15650)
"""
문제 설명
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
- 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
- 고른 수열은 오름차순이어야 한다.
"""

# 내 풀이
import sys
n, m = map(int, sys.stdin.readline().split())
select = []
final = []

def calculate() :
    if len(select) == m :
        select_sort = sorted(select)
        if select_sort not in final :
            final.append(select_sort)
        return
    
    for i in range(1, n + 1) :
        if i not in select :
            select.append(i)
            calculate()
            select.pop()

calculate()
for i in final :
    print(' '.join(map(str, i)))

"""
insight 정리
1. 백트래킹의 가장 기본적인 문제. 처음에는 막막했는데, 기초 뼈대를 알고 난 후에는 너무 어렵지는 않았음. 오히려 개념이 어려웠음
2. 백트래킹은 dfs 및 브루트포스와 공통점이 있는 알고리즘. 상태 기반 트리를 베이스로 주어진 문제에 맞는 상황을 탐색하며, 거의 모든 경우를 고려하지만 불필요하다고 판단되는 탐색을 하지 않는다
탐색 -> dfs, 거의 모든 경우 고려 -> 브루트포스가 각각 연관 된다고 이해하면 됨.
3. 특정 공간에서 필요한 탐색이 모두 끝난 후, 다음 공간으로 어떻게 이동시키느냐가 구현 난이도를 높현던 이유였음. 이 문제는 stack을 베이스로 구현하면 됨
"""