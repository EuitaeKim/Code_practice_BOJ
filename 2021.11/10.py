# 1. 2670 - 연속부분최대곱 (https://www.acmicpc.net/problem/2670)
"""
문제 설명
N개의 실수가 있을 때, 한 개 이상의 연속된 수들의 곱이 최대가 되는 부분을 찾아,
그 곱을 출력하는 프로그램을 작성하시오.
"""

# 내 풀이
import sys
n = int(sys.stdin.readline())
li = [float(sys.stdin.readline()) for _ in range(n)]

def dp(list) :
    if len(list) == 1 :
        return list[0]
    for i in list :
        return i * dp(list[1:])

final = max(li)
for j in range(2, len(li)+1) :
    for i in range(0, len(li)-j+1) :
        result = dp(li[i:i+j])
        if final < result :
            final = result

print(round(final, 4))

# Case Study
import sys
n = int(sys.stdin.readline().strip())
arr = [-1]
dp = [-1] * (n+1)

for _ in range(n):
    data = float(sys.stdin.readline().strip())
    arr.append(data)

for i in range(1, n+1):
    if dp[i-1] > 1:
        dp[i] = dp[i-1] * arr[i]
    else:
        dp[i] = arr[i]

max_val = -987654321
for i in range(n):
    max_val = max(max_val, dp[i])

print('{0:.3f}'.format(max_val))

"""
insight 정리
1. 기존에 알고 있던 다이나믹 프로그래밍 틀에서 벗어난 문제를 만나고 길을 잃음.. DP에서 꼭 재귀를 써야하는건 아니다.
2. 가뜩이나 파이썬은 재귀에 적합하지 않은 언어인데, 괜히 재귀 많이 쓰다가 콜 스택 쌓여버리면 더 비효율적인 것 같음
3. 아직 Case Study에 대한 이해가 잘 안되서 꼭 반복해서 풀어볼 것
"""