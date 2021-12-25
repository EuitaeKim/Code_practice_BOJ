# 1. 7569 - 토마토 (https://www.acmicpc.net/problem/7569)
"""
문제 설명
토마토를 창고에 보관하는 격자모양의 상자들의 크기와 익은 토마토들과 익지 않은 토마토들의 정보가 주어졌을 때,
며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수를 구하는 프로그램을 작성하라.
단, 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있다.
"""

# 내 풀이
import sys
from collections import deque
input = sys.stdin.readline

graph = []
count = 0
m, n, h = map(int, input().split())

for _ in range(h) :
    graph_2 = []
    for _ in range(n) :
        li = list(map(int, input().split()))
        for i in li :
            if i == 1 or i == - 1 :
                count += 1
        graph_2.append(li)
    graph.append(graph_2)

que = deque([])
if count == m * n * h :
    print(0)
else :
    for i in range(h) :
        for j in range(n) :
            for k in range(m) :
                if graph[i][j][k] == 1 :
                    que.append((i, j, k))

    que_2 = deque([])
    day = 0
    while True :
        start = que.popleft()
        f = start[0]
        s = start[1]
        t = start[2]
        if f - 1 > - 1 and graph[f - 1][s][t] == 0 :
            graph[f - 1][s][t] = 1
            que_2.append((f - 1, s, t))
        if f + 1 < h and graph[f + 1][s][t] == 0 :
            graph[f + 1][s][t] = 1
            que_2.append((f + 1, s, t))
        if s - 1 > - 1 and graph[f][s - 1][t] == 0 :
            graph[f][s - 1][t] = 1
            que_2.append((f, s - 1, t))
        if s + 1 < n and graph[f][s + 1][t] == 0 :
            graph[f][s + 1][t] = 1
            que_2.append((f, s + 1, t))
        if t - 1 > - 1 and graph[f][s][t - 1] == 0 :
            graph[f][s][t - 1] = 1
            que_2.append((f, s, t - 1))
        if t + 1 < m and graph[f][s][t + 1] == 0 :
            graph[f][s][t + 1] = 1
            que_2.append((f, s, t + 1))
    
        if len(que) == 0 :
            if len(que_2) == 0 :
                break
            else :
                que = que_2
                day += 1
                que_2 = deque([])

    break_check = False
    for i in range(h) :
        for j in range(n) :
            for k in range(m) :
                if graph[i][j][k] == 0 :
                    break_check = True
                    print(-1)
                    break
            if break_check :
                break
        if break_check :
            break

    if not break_check :
        print(day)


# Case Study
import sys
from collections import deque
m, n, h = map(int,input().split())
graph = []
queue = deque([])
 
for i in range(h):
    tmp = []
    for j in range(n):
        tmp.append(list(map(int,sys.stdin.readline().split())))
        for k in range(m):
            if tmp[j][k]==1:
                queue.append([i,j,k])
    graph.append(tmp)
    
dx = [-1,1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

while(queue):
    x,y,z = queue.popleft()
    
    for i in range(6):
        a = x+dx[i]
        b = y+dy[i]
        c = z+dz[i]
        if 0<=a<h and 0<=b<n and 0<=c<m and graph[a][b][c]==0:
            queue.append([a,b,c])
            graph[a][b][c] = graph[x][y][z]+1
            
day = 0
for i in graph:
    for j in i:
        for k in j:
            if k==0:
                print(-1)
                exit(0)
        day = max(day,max(j))
print(day-1)

"""
insight 정리
1. 98%에서 out of index error뜬 내 코드 -> 내 코드보다 훨 ~~~~~~~~~ 씬 간결하고 답도 잘 나오는 코드
2. 3중 for문에서 빠져나올 때 exit(0) 쓰는 것, 입력과 동시에 deque의 최초 list를 만드는 것, 특히 6방향 값을 판정하는 과정은 꼭 벤치마킹하기
3. 또한 Case에서는 graph에 day값을 입력하는 방식을 활용하고 있음도 체크하기
"""