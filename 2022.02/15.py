# 1. 1916 - 최소비용 구하기 (https://www.acmicpc.net/problem/1916)
"""
문제 설명
N개의 도시가 있다. 그리고 한 도시에서 출발하여 다른 도시에 도착하는 M개의 버스가 있다.
우리는 A번째 도시에서 B번째 도시까지 가는데 드는 버스 비용을 최소화 시키려고 한다.
A번째 도시에서 B번째 도시까지 가는데 드는 최소비용을 출력하여라. 도시의 번호는 1부터 N까지이다.
"""

# Case Study
import sys
import heapq
from collections import defaultdict
input=sys.stdin.readline

N=int(input()); M=int(input())

# 하나의 key에 여러 value를 넣기 위해 기본 dict를 생성
# 인자로 주어진 list를 초깃값으로 설정
graph=defaultdict(list)

# 최초 거리는 INF로 설정
# 최종 연산 결과도 INF로 남아있을 경우, 경로가 없다는 것을 의미한다.
distances=[1e9]*(N+1)

# 시작 노드,종료 노드,가중치 받기
# 값을 변경하지 않으므로 속도를 고려하여 tuple을 사용
for _ in range(M):
    s,e,c=map(int,input().split())
    graph[s].append((e,c))

# 시작, 종료 값 받기
start,end=map(int,input().split())

def dijkstra(start):
    queue=[]
    # 최초 비용 값과 시작 지점을 큐에 삽입
    heapq.heappush(queue,(0,start))

    # 우선순위 큐를 쓰는 이유. 속도에 이점이 있다.
    # 내가 참고했던 자료: http://jaegualgo.blogspot.com/2017/07/dijkstra-priority-queue.html
    # 쉽게 생각하면 A > x > B로 가는 경우가 여러 개 있고, 각 경우 별 비용이 10, 9, 8, 7, 6, 5이며,
    # 이 순서대로 최소 거리를 계산할 경우, 9 갱신 ~ 5 갱신을 일일히 해야 한다.
    # 그러나 우선순위 큐를 사용하면 5로 갱신한 이후 나머지 계산은 pass한다.
    # 이 계산을 하는 부분이 46 ~ 63 라인이다.

    while queue:
        dist,now=heapq.heappop(queue)
        # pop 한 노드까지의 거리가 기존에 저장되어 있는 값보다 클 경우
        # 다음 연산 없이 pass 한다. (할 필요가 없기 때문에!)
        if distances[now]<dist:
            continue
        # pop 한 노드와 연결되어 있는 노드 탐색
        for node in graph[now]:
            # cost = now까지 오는데 걸린 비용 + 연결되어 있는 노드로 가는 비용
            # node[1]->비용, node[0]->도착 노드
            cost=dist+node[1]
            # 이 cost가 기존에 저장되어 있는 값보다 작을 경우 갱신한다.
            if distances[node[0]]>cost:
                distances[node[0]]=cost
                # 다음 노드를 탐색하기 위해 가장 마지막 노드와 계산된 cost 값을 입력
                # 기존 값보다 더 작을 경우에만 큐에 넣는다는 점을 체크
                heapq.heappush(queue,(cost,node[0]))

dijkstra(start)
print(distances[end])

"""
insight 정리
1. 다익스트라 문제를 이번에 처음 풀어봤는데 어렵다.. VScode Preview로 계속 돌려봐도 이해가 안된다..
최소한의 힌트만 갖고 최대한 풀어보려고 했는데 몇일을 보내버려서 포기..
2. 이번에 최대한 분석해보고 다음에 유사 문제를 꼭 풀어보아야 함. 아직 50%도 체화하지 못함.
"""