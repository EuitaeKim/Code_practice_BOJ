# 1. 15663 - N과 M (9) (https://www.acmicpc.net/problem/15663)
"""
문제 설명
N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
N개의 자연수 중에서 M개를 고른 수열
"""

# 내 풀이
import sys
input=sys.stdin.readline
n, m=map(int, input().split())
li=list(map(int, input().split()))
li.sort()

li_co=[0]*10001
for i in li:
    li_co[i]+=1

final={}
result=[]
def check():
    if len(result)==m and tuple(result) not in final:
        print(' '.join(map(str, result)))
        final[tuple(result)]=1
    else:
        for i in li:
            if li_co[i]-1 >=0:
                result.append(i)
                li_co[i]-=1
                check()
                result.pop()
                li_co[i]+=1

check()

"""
insight 정리
1. 3중 조건문을 무리하게 쓰다가 시간 초과, 해시가 아닌 리스트로 final 변수를 활용하다 시간 초과, 무한 로프로 인한 런타임 오류 등등..
의도치 않게 많은 오류를 겪어버린 문제..
2. 백트래킹을 써야할 때 결과 값을 겹치치 않게 뽑아내는 방법, 주어진 수의 개수만큼만 활용하여 뽑아내는 방법을 구현해야 한다면 참고할 것
"""