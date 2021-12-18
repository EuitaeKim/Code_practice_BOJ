# 1. 14889 - 스타트와 링크 (https://www.acmicpc.net/problem/14889)
"""
문제 설명
오늘은 스타트링크에 다니는 사람들이 모여서 축구를 해보려고 한다. 축구는 평일 오후에 하고 의무 참석도 아니다.
축구를 하기 위해 모인 사람은 총 N명이고 신기하게도 N은 짝수이다. 이제 N/2명으로 이루어진 스타트 팀과 링크 팀으로 사람들을 나눠야 한다.

BOJ를 운영하는 회사 답게 사람에게 번호를 1부터 N까지로 배정했고, 아래와 같은 능력치를 조사했다.
능력치 Sij는 i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치이다.
팀의 능력치는 팀에 속한 모든 쌍의 능력치 Sij의 합이다. Sij는 Sji와 다를 수도 있으며,
i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치는 Sij와 Sji이다.

축구를 재미있게 하기 위해서 스타트 팀의 능력치와 링크 팀의 능력치의 차이를 최소로 하려고 한다.
"""

# 내 풀이
import sys
from itertools import combinations

input = sys.stdin.readline
n = int(input())
synergy = [list(map(int, input().split())) for _ in range(n)]

all = [i for i in range(1, n + 1)]
team_1_raw = list(combinations(all, n // 2))

team_1 = []
team_2 = []
for i in team_1_raw :
    j = list(i)
    team_1.append(j)
    k = list(set(all) - set(j))
    team_2.append(k)

diff = 999999
for i, j in zip(team_1, team_2) :
    team_1_sum = 0
    team_2_sum = 0
    for k in i :
        for y in i :
            team_1_sum += synergy[k - 1][y - 1]

    for k in j :
        for y in j :
            team_2_sum += synergy[k - 1][y - 1]
    
    diff = min(abs(team_1_sum - team_2_sum), diff)

print(diff)

"""
insight 정리
1. 백트래킹에 브루트포스가 붙은 문제여서 쉽게 풀릴 줄 알았는데, 시간초과로 고생했던 문제
2. 35 ~ 44 line이 3중 for 문이어서 시간초과의 원인인 것 같은데, 수정 방향성이 떠오르지 않아 pypy3으로 제출하여 통과함 (다시 수정을 시도해봐야 함)
3. 또한 permutation, combination을 구현해야 할 경우, 알고리즘 연습때는 백트래킹을 직접 구현하지만 실전에서는 라이브러리를 적극 활용할 것 (좋은 도구는 적극 활용하겠다는 의미) 
"""