# 1. 9251 - LCS (https://www.acmicpc.net/problem/9251)
"""
문제 설명
LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때,
모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.
예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.
첫째 줄과 둘째 줄에 두 문자열이 주어진다. 문자열은 알파벳 대문자로만 이루어져 있으며, 최대 1000글자로 이루어져 있다.
"""

# 내 풀이
import sys
input=sys.stdin.readline
m=str(input().rstrip()); n=str(input().rstrip())
dp=[[0]*(len(m)+1) for _ in range(len(n)+1)]

for idx_i, i in enumerate(m):
    for idx_j, j in enumerate(n):
        if i==j:
            dp[idx_j+1][idx_i+1]=dp[idx_j][idx_i]+1
        else:
            dp[idx_j+1][idx_i+1]=max(dp[idx_j][idx_i+1], dp[idx_j+1][idx_i])

print(max(max(dp)))

"""
insight 정리
1. https://bit.ly/3J42gjG 개념이 정말 잘 정리되어 있는 포스트 참고하면서 복습할 것.
2. 이번 문제는 최장 길이만 구하면 되지만, 최장 공통 문자열을 구해야 하는 경우, 실제 수열까지 찾아내는 방법 등
다양하게 변형되어 문제로 나올 가능성이 큼
"""