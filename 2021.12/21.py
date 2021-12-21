# 1. 1260 - DFS와 BFS (https://www.acmicpc.net/problem/1260)
"""
문제 설명
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.
"""

# 내 풀이
import sys
from collections import deque

input = sys.stdin.readline
n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m) :
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

for i in graph :
    i.sort(reverse = True)

stack = [v]
dfs = []

while stack :
    start = stack.pop()
    if start not in dfs :
        dfs.append(start)
    for node in graph[start] :
        if node not in dfs :
            stack.append(node)

print(' '.join(map(str, dfs)))

for i in graph :
    i.sort()
    
que = deque([v])
bfs = []
check = [0 for _ in range(n + 1)]

while que :
    start = que.popleft()
    if start not in bfs :
        bfs.append(start)
        check[start] = 1
    for node in graph[start] :
        if check[node] == 0 :
            que.append(node)
            check[node] = 1

print(' '.join(map(str, bfs)))

# Case Study
import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())
temp = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
graph = [[]for _ in range(N+1)]

def dfs(v, graph, visited):
    visited[v] = True
    print(v, end = ' ')

    for idx in graph[v]:
        if not visited[idx]:
            dfs(idx, graph, visited)

def bfs(v, graph, visited):
    queue = deque([v])
    visited[v] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for idx in graph[v]:
            if not visited[idx]:
                queue.append(idx)
                visited[idx] = True

for idx in temp:
    a, b = idx
    graph[a].append(b)
    graph[b].append(a)

for idx in range(len(graph)):
    graph[idx].sort()

visited = [False] * (N+1)
dfs(V, graph, visited)
print()
visited = [False] * (N+1)
bfs(V, graph, visited)

"""
insight 정리
1. 문제는 맞았지만 재귀를 활용한 풀이법도 알아야 할 것 같아서 기록해두기!
"""