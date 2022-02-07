# 1. 12851 - 숨바꼭질 2 (https://www.acmicpc.net/problem/12851)
"""
문제 설명
수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고,
동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다.
만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다.
순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 그리고,
가장 빠른 시간으로 찾는 방법이 몇 가지 인지 구하는 프로그램을 작성하시오.
"""

# 내 풀이
import sys
from collections import deque
input=sys.stdin.readline
n,k=map(int, input().split())
que=deque([n])
que_2=[]
count=[0]*100000
result=[0]*100000
check=False

def bfs():
    while que:       
        global result, count, check
        s=que.popleft()
        li=[s+1,s-1,s*2]
        for i in li:
            if i==k:
                check=True
            try:
                result[i]=result[s]+1
                count[i]=count[s]+1
                que_2.append(i)
            except:
                pass

if n==k: print(0, 1, sep='\n')
elif n>k: print(n-k, 1, sep='\n')
else:
    while True:
        bfs()
        if check: break
        else:
            que=deque(list(que_2))
            que_2=[]
    print(count[k], result[k], sep='\n')

# Case Study
import sys
from collections import defaultdict
n,k=map(int,sys.stdin.readline().split())
vis=defaultdict(lambda:0)
queue=[n]
find=False

turn_count=0
path_num=0

if n==k: print(0,1,sep='\n')
elif n>k: print(n-k,1,sep='\n')
else:
    while find==False:
        turn_count+=1
        queue_temp=[]
        while queue:
            num=queue.pop()
            x=[num-1, num+1, num*2]

            if k not in x:
                for i in x:
                    if 100000>=i>=0 and (turn_count==vis[i] or not vis[i]):
                        queue_temp.append(i)
                        vis[i]=turn_count
            
            else:
                find = True
                for i in x:
                    if i == k:
                        path_num+=1
        queue=queue_temp
    print(turn_count,path_num,sep='\n')

"""
insight 정리
1. 일반적인 bfs 유형의 문제와 달랐던 것은, 모든 경우의 수를 고려하면 메모리 초과가 나타난다는 것이었음
2. 1에 대한 보완 및 문제에서 요구하는 결과가 2가지였기 때문에, 이에 대한 정보를 얻고자 다양한 변수를 설정하였음
3. 전체적으로 아이디어는 도출할 수 있었으나, 73줄의 turn_count==vis[i] 코드 의미를 파악하지 못했음. 대표적인 사례로 1 4가 주어졌을 때.
4. 또한 같은 줄의 100000>=i>=0의 의미도 파악하지 못했던 점을 체크할 것
5. 약간 dp 개념이 섞인 bfs 문제로도 볼 수 있을 듯
"""