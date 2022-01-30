# 1. 9465 - 스티커 (https://www.acmicpc.net/problem/9465)
"""
문제 설명
상근이의 여동생 상냥이는 문방구에서 스티커 2n개를 구매했다. 스티커는 그림 (a)와 같이 2행 n열로 배치되어 있다.
상냥이는 스티커를 이용해 책상을 꾸미려고 한다.
상냥이가 구매한 스티커의 품질은 매우 좋지 않다. 스티커 한 장을 떼면,
그 스티커와 변을 공유하는 스티커는 모두 찢어져서 사용할 수 없게 된다.
즉, 뗀 스티커의 왼쪽, 오른쪽, 위, 아래에 있는 스티커는 사용할 수 없게 된다.
모든 스티커를 붙일 수 없게된 상냥이는 각 스티커에 점수를 매기고, 점수의 합이 최대가 되게 스티커를 떼어내려고 한다.
"""

# 내 풀이
import sys
input=sys.stdin.readline
for _ in range(int(input())):
    n=int(input())
    dp=[list(map(int, input().split())) for _ in range(2)]
    if n==1: print(max(dp[0][0], dp[1][0]))
    elif n==2: print(max(dp[0][0]+dp[1][1], dp[0][1]+dp[1][0]))
    else:
        t=2
        while True:
            dp[1][t]+=max(dp[0][t-1]+dp[1][t-2], dp[0][t-2])
            dp[0][t]+=max(dp[1][t-1]+dp[0][t-2], dp[1][t-2])

            if t+2<=n-1: t+=2
            else:
                if t+1==n-1:
                    t+=1
                    dp[1][t]+= dp[0][t-1]
                    dp[0][t]+= dp[1][t-1]
                    break
                else:
                    break
        print(max(dp[0][n-1], dp[1][n-1]))

# Case Study
t = int(input())
for i in range(t):
  s = []
  n = int(input())
  for k in range(2):
    s.append(list(map(int, input().split())))
  for j in range(1, n):
    if j == 1:
      s[0][j] += s[1][j - 1]
      s[1][j] += s[0][j - 1]
    else:
      s[0][j] += max(s[1][j - 1], s[1][j - 2])
      s[1][j] += max(s[0][j - 1], s[0][j - 2])
  print(max(s[0][n - 1], s[1][n - 1]))


"""
insight 정리
1. 규칙은 찾았으나, 1단위가 아닌 2단위로만 해결하려 하느라(내 풀이에서는 t, Case Study에서는 j) 문제 풀이도 못하고 코드도 불필요하게 복잡해진 문제
2. 생각만 조금 유연하게 했으면 금방 풀 수 있었을텐데.. 점화식을 명확히 찾았는데 문제를 맞추지 못하고 있다면, 잠깐 생각을 환기시키고 다시 볼 것
"""