# 1. 15652 - N과 M (4) (https://www.acmicpc.net/problem/15652)
"""
문제 설명
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
- 1부터 N까지 자연수 중에서 M개를 고른 수열
- 같은 수를 여러 번 골라도 된다.
- 고른 수열은 비내림차순이어야 한다.
"""

# 내 풀이
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
li = [i for i in range(1, n+1)]
check = [0]*(n+1)

re = []
def back() :
    if len(re) == m :
        ch = False
        for i in range(1, len(re)) :
            if re[i-1] > re[i] :
                ch = True
                return
        if not ch :
            print(' '.join(map(str, re)))
            return

    else :
        for k in li :
            if check[k] < m :
                re.append(k)
                check[k] += 1
                back()
                re.pop()
                check[k] -= 1
        return
back()

# Case Study
n, m = map(int, input().split())
s = []

def dfs():
    if len(s) == m:
        print(*s)
        return
    
    for i in range(1, n+1):
        if s and i < s[-1]:
            continue
        s.append(i)
        dfs()
        s.pop()
        
dfs()

"""
insight 정리
1. 코드 작성의 효율성을 높이기 위해 자잘한 코드 작성 팁을 기록해놓기
"""