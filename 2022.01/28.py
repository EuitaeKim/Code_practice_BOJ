# 1. 7662 - 이중 우선순위 큐 (https://www.acmicpc.net/problem/7662)
"""
문제 설명
정수만 저장하는 이중 우선순위 큐 Q가 있다고 가정하자.
Q에 저장된 각 정수의 값 자체를 우선순위라고 간주하자. 
Q에 적용될 일련의 연산이 주어질 때 이를 처리한 후 최종적으로
Q에 저장된 데이터 중 최댓값과 최솟값을 출력하는 프로그램을 작성하라.
"""

# Case Study
import sys
input=sys.stdin.readline
import heapq

result=[]
for _ in range(int(input())):
    vis=[0]*1000001
    min_heap,max_heap=[],[]
    for i in range(int(input())):
        s=input().split()
        if s[0]=='I':
            heapq.heappush(min_heap,(int(s[1]),i))
            heapq.heappush(max_heap,(-int(s[1]),i))
            vis[i]=1
        elif s[1]=='1':
            while max_heap and not vis[max_heap[0][1]]:
                heapq.heappop(max_heap)
            if max_heap:
                vis[max_heap[0][1]]=0
                heapq.heappop(max_heap)
        else:
            while min_heap and not vis[min_heap[0][1]]:
                heapq.heappop(min_heap)
            if min_heap:
                vis[min_heap[0][1]]=0
                heapq.heappop(min_heap)
    while min_heap and not vis[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not vis[max_heap[0][1]]:
        heapq.heappop(max_heap)
    result.append(f'{-max_heap[0][0]} {min_heap[0][0]}'if max_heap and min_heap else'EMPTY')
print('\n'.join(result))

"""
insight 정리
1. 최소 힙만 모듈을 통해 구현할 수 있는 파이썬에서 최소, 최대 힙을 동시에 활용할 수 있는 방법에 관한 문제.
2. 데이터에 유일성을 부여하는 아이디어, 서로 다른 힙에 저장되는 데이터의 동기화 방법에 대한 지속적인 복습이 필요!
"""