# 1. 11403 - 경로 찾기 (https://www.acmicpc.net/problem/11403)
"""
문제 설명
가중치 없는 방향 그래프 G가 주어졌을 때, 모든 정점 (i, j)에 대해서,
i에서 j로 가는 경로가 있는지 없는지 구하는 프로그램을 작성하시오.
"""

# Case Study
n = int(input())
visit = [0 for _ in range(n)]

s = []
for i in range(n):
    s.append(list(map(int, input().split())))

def dfs(v):
    for i in range(n):
        if visit[i] == 0 and s[v][i] == 1:
            visit[i] = 1
            dfs(i)

for i in range(n):
    dfs(i)
    for j in range(n):
        if visit[j] == 1:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()
    visit = [0 for _ in range(n)]

# Case Study
import sys
input = sys.stdin.readline
N = int(input())
graph = []

for _ in range(N) :
    graph.append(list(map(int,input().split())))
    
for k in range(N) :
    for i in range(N) :
        for j in range(N) :
            if graph[i][k] and graph[k][j] :
                graph[i][j] = 1

for r in graph :
    for c in r :
        print(c, end = " ")
    
    print()

"""
insight 정리
1. (첫 번째 Case) dfs로 방문을 했는지 안했는지 판별
 > i -> j로의 루트가 하나 발견되면, dfs로 끝까지 따라가서 i -> x의 모든 경우의 수를 체크
 > dfs 하면 list + stack 만 생각했었다 보니 Case와 같은 해결 방법을 생각하지 못함. definition, check 등을 잘 활용하기
 > 또한 복습할 때 i -> i가 어떻게 판별될 수 있었는지를 다시 떠올려보기

2 (두번째 Case) 플로이드 와샬 알고리즘을 사용하여 어느 한 곳에 들려 다른 곳으로 가는 길이 존재한다면 그 값을 체킹
 > 알고리즘은 굉장히 간단하며, k 값이 최상단에 와야 한다는 점만 기억하기
 > 다만 graph를 실시간으로 변경하고 전체 cycle을 한 번만 탐색하는데 모든 경우의 수가 체크 될 수 있다는게 이해되지 않음.
 > 그래서 사이클을 두번 돌려봤는데 결과 동일. 이게 왜 가능한지 이해가 안되서 관련 문제를 풀어보면서 개념을 찾아봐야 함
"""