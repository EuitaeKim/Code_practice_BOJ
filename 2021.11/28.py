# 1. 11659 - 구간 합 구하기 4 (https://www.acmicpc.net/problem/11659)
"""
문제 설명
수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성하시오.
첫째 줄에 수의 개수 N과 합을 구해야 하는 횟수 M이 주어진다. 둘째 줄에는 N개의 수가 주어진다.
수는 1,000보다 작거나 같은 자연수이다. 셋째 줄부터 M개의 줄에는 합을 구해야 하는 구간 i와 j가 주어진다.

제한
1 ≤ N ≤ 100,000
1 ≤ M ≤ 100,000
1 ≤ i ≤ j ≤ N
"""

# 내 풀이
import sys
a, b = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))

for _ in range(b) :
    result = 0
    s, e = map(int, sys.stdin.readline().split())
    for i in range(s-1, e) :
        result += li[i]
    print(result)

# Case Study
import sys
a, b = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))

for idx, i in enumerate(li) :
    if idx != 0 :
        li[idx] += li[idx - 1] 

for _ in range(b) :
    s, e = map(int, sys.stdin.readline().split())
    if s == 1 :
        print(li[e-1])
    else :
        print(li[e-1] - li[s-2])

"""
insight 정리
1. 두 코드 모두 정상적으로 답을 도출하지만 내 풀이 코드는 시간초과, Case Study로 수정한 코드는 정답처리 됨. 두 코드의 차이는
부분 합을 구할 때 기존 list를 slicing해서 구하느냐, 기존 list를 누적 합으로 업데이트 한 후 범위의 시작과 끝 index만을 활용하느냐임
2. 최악의 경우는 10만개의 list값을 10만번 연산하는 경우. 각 연산 별 10만 범위를 내 풀이에서 연산해야 한다면 10만 * 10만의 연산을 진행 해야 함
3. 그러나 Case Study로 수정한 코드는 누적 합을 구하기 위한 10만번 연산 + 10만번 연산 * 2번의 연산을 진행해야 함
4. 결국 특정 구간의 합을 구하기 위해선 누적 값을 적극 활용하는 것이 좋음
"""
