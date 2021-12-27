# 1. 1931 - 회의실 배정 (https://www.acmicpc.net/problem/1931)
"""
문제 설명
한 개의 회의실이 있는데 이를 사용하고자 하는 N개의 회의에 대하여 회의실 사용표를 만들려고 한다.
각 회의 I에 대해 시작시간과 끝나는 시간이 주어져 있고, 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수를 찾아보자.
단, 회의는 한번 시작하면 중간에 중단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다.
회의의 시작시간과 끝나는 시간이 같을 수도 있다. 이 경우에는 시작하자마자 끝나는 것으로 생각하면 된다.
"""

# 내 풀이
import sys
input = sys.stdin.readline
n = int(input())
li = []
for _ in range(n) :
    li.append(list(map(int, input().split())))

li.sort(key = lambda x : (x[1], x[0]))

times = [-1, -1]
count = 0
for time in li :
    if times[1] <= time[0] :
        times = time
        count += 1

print(count)

"""
insight 정리
1. greedy하게 회의실을 배정하는 방법에 대한 아이디어가 떠오르지 않았던 문제
2. 끝 시간 -> 시작 시간으로 데이터를 정렬했던 이유 및 22 ~ 25줄의 코드가 greedy하게 적용되는 이유를 이해하고 복습하기
"""