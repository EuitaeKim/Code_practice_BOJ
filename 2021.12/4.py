# 1. 18352 - 특정 거리의 도시 찾기 (https://www.acmicpc.net/problem/18352)
"""
문제 설명
어떤 나라에는 1번부터 N번까지의 도시와 M개의 단방향 도로가 존재한다. 모든 도로의 거리는 1이다.
이 때 특정한 도시 X로부터 출발하여 도달할 수 있는 모든 도시 중에서, 최단 거리가 정확히 K인 모든 도시들의 번호를 출력하는 프로그램을 작성하시오.
또한 출발 도시 X에서 출발 도시 X로 가는 최단 거리는 항상 0이라고 가정한다.
"""

# Case Study
from collections import deque

# 도시의 개수, 도로의 개수, 거리 정보, 출발 도시 정보
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

# 모든 도로 정보 입력 받기
for _ in range(m) : 
    a, b = map(int, input().split())
    graph[a].append(b)

# 모든 도시에 대한 최단 거리 초기화
distance = [-1] * (n + 1)
# 출발 도시까지의 거리는 0으로 설정
distance[x] = 0

# 너비 우선 탐색 수행
q = deque([x])
while q :
    now = q.popleft()
    # 현재 도시에서 이동할 수 있는 모든 도시를 확인
    for next_node in graph[now] :
        # 아직 방문하지 않은 도시라면
        if distance[next_node] == -1 :
            # 최단 거리 갱신
            distance[next_node] = distance[now] + 1
            q.append(next_node)

# 최단 거리가 K인 모든 도시의 번호를 오름차순으로 출력
check = False
for i in range(1, n + 1) :
    if distance[i] == k :
        print(i)
        check = True

# 만약 최단 거리가 k인 도시가 없다면, -1 출력
if check == False :
    print(-1)

"""
insight 정리
1. 혼자 BFS 구조 짜보려고 몇 일 시간 쓰다가 도저히 안되서 나동빈님 유튜브 채널에서 소개 받은 문제를 바탕으로 BFS의 기본 베이스를 잡은 문제
2. BFS 구조 짤 때 방문한 도시를 체크하는 방법, 이중 리스트에서 값이 없는 인덱스를 부여 받았을 때의 작동방식 등 헷갈리는 부분이 많았는데 해당 구조를 통해 해결할 수 있었음.
3. 혼자서 고민해보는 것은 좋지만 새로운 개념을 막 적용해보기 시작하는 시기에 몇 날 몇일 동안 해결이 안된다면, 오히려 기본 뼈대 코드를 익히고 시작하는게 더 나을수도 있겠다는 생각이 듦
"""