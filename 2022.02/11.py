# 1. 2493 - 탑 (https://www.acmicpc.net/problem/2493)
"""
문제 설명
KOI 통신연구소는 레이저를 이용한 새로운 비밀 통신 시스템 개발을 위한 실험을 하고 있다.
실험을 위하여 일직선 위에 N개의 높이가 서로 다른 탑을 수평 직선의 왼쪽부터 오른쪽 방향으로 차례로 세우고,
각 탑의 꼭대기에 레이저 송신기를 설치하였다. 모든 탑의 레이저 송신기는 레이저 신호를 지표면과 평행하게 수평 직선의 왼쪽 방향으로 발사하고,
탑의 기둥 모두에는 레이저 신호를 수신하는 장치가 설치되어 있다. 하나의 탑에서 발사된 레이저 신호는 가장 먼저 만나는 단 하나의 탑에서만 수신이 가능하다.
탑들의 개수 N과 탑들의 높이가 주어질 때, 각각의 탑에서 발사한 레이저 신호를 어느 탑에서 수신하는지를 알아내는 프로그램을 작성하라.
"""

# 내 풀이
import sys
input=sys.stdin.readline
n=int(input())
li=list(map(int, input().split()))

result=[0]*n
while li:
    start=li.pop()
    start_ind=len(li)
    order_num=0
    while True:
        if abs(order_num-1)<=start_ind:
            order_num -=1
        else: break

        if li[order_num]>start:
            result[start_ind]=li.index(li[order_num])+1
            break

print(' '.join(map(str, result)))

# Case Study
import sys
input=sys.stdin.readline
n=int(input())
li=list(map(int, input().split()))
stack=[]
answer=[]

# 탑의 개수만큼 반복문을 돌린다.
for i in range(n):
    # 최댓값 관련 정보가 없을 때까지 비교를 진행한다.
    while stack:
        # 왼쪽탑이 오른쪽 탑보다 크기가 크면
        if stack[-1][1]>li[i]:
            # 결과 인덱스 저장
            answer.append(stack[-1][0]+1)
            # 원하는 답을 구했으므로 반복문 종료
            break
        else:
            # 답을 못 찾을 경우 비교한 최댓값을 뺀 후 다음 최댓값과 비교한다.
            stack.pop()
    # 스택이 빌 때까지 답을 못 찾는다면, 0을 넣는다.
    if not stack:
        answer.append(0)
    # 왼쪽 값보다 오른쪽 갑이 크다면, 왼쪽 값은 삭제되고 오른쪽 값은 삽입된다.
    # 오른쪽 값보다 왼쪽 값이 크다면, 왼쪽 값을 보존한 채로 오른쪽 값을 삽입한다.
    stack.append([i, li[i]])

print(" ".join(map(str, answer)))

"""
insight 정리
1. 내 풀이의 문제점: 최악의 경우 50만 개의 수를 담은 리스트를 계속 완전 탐색해야 한다.
2. 개선 방향: 완전 탐색은 비효율적이다. O(n^2)을 O(n)으로 해결할 아이디어가 필요하다.
3. 개선 아이디어: 기존 오른쪽->왼쪽 탐색 순서를 왼쪽->오른쪽 탐색으로 바꾸면 최댓값을 기준으로 한 효율적인 비교가 가능하다.
    -> (Case Study) 답을 출력하기 위한 List(answer, 신호 받는 탑 위치 인덱스),
    최댓값과 그 위치를 저장하는 List(stack, 신호 받는 탑 위치 인덱스+최댓값)를 활용한다.
4. 이전까지 떠올려보지 못한 아이디어라 반복 숙달이 필요한..
"""