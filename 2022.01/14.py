# 1. 17433 - 신비로운 수 (https://www.acmicpc.net/problem/17433)
"""
문제 설명
0이 아닌 정수 N개가 주어졌을 때, 0이 아닌 정수 M이 다음 성질을 만족하면 M은 N개의 정수에 대해 신비로운 수라고 한다.
- N개의 정수를 M으로 나눈 나머지가 모두 같다.
임의의 N개의 정수에 대해 신비로운 수는 적어도 하나 이상 존재한다.
예를 들어, 1은 N개의 정수와 상관없이 항상 신비로운 수이다.
N개의 수가 주어졌을 때, N개의 정수에 대해 신비로운 수 중에서 가장 큰 수를 구해보자.
"""

# 내 풀이
import sys
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    n=int(input())
    li=list(map(int,input().split()))
    if len(set(li)) == 1:
        print('INFINITY')
    else:
        for i in range(max(li), 0, -1):
            start=li[0]%i
            check=True
            for j in li:
                if j%i != start:
                    check=False
                    break
            if check:
                print(i)
                break

# Case Study
import sys
read = sys.stdin.readline

def GCD(x, y):
    while y != 0:
        x, y = y, x % y
    return x

for _ in range(int(read())):
    n = int(read())
    num = list(map(int, read().split()))
    num.sort()
    diff = set()
    for i in range(1, n):
        diff.add(num[i]-num[i-1])
    diff = list(diff)

    if diff == [0]:
        print('INFINITY')
        continue

    x = diff[0]
    for i in range(1, len(diff)):
        tmp = GCD(x, diff[i])
        x = tmp
    print(x)

"""
insight 정리
1. 주어진 수들의 차이의 최대 공약수를 구하면 된다.
    -> a % m = x, b % m = x라면, (a-b) % m = 0이다.
    -> 두 수의 차가 m의 배수일 때 두 수를 m으로 나누면 나머지가 같아진다.
    -> 숫자들이 주어졌을 때, 각 숫자들의 차를 구하고 이 차들의 최대공약수를 구한다.
    -> 이때 각 차들이 모두 0인 경우 숫자들이 같으므로 INFINITY를 갖는다.
"""