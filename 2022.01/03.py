# 1. 1107 - 리모컨 (https://www.acmicpc.net/problem/1107)
"""
문제 설명
수빈이는 TV를 보고 있다. 수빈이는 채널을 돌리려고 했지만, 버튼을 너무 세게 누르는 바람에, 일부 숫자 버튼이 고장났다.
리모컨에는 버튼이 0부터 9까지 숫자, +와 -가 있다. +를 누르면 현재 보고있는 채널에서 +1된 채널로 이동하고,
-를 누르면 -1된 채널로 이동한다. 채널 0에서 -를 누른 경우에는 채널이 변하지 않고, 채널은 무한대 만큼 있다.
수빈이가 지금 이동하려고 하는 채널은 N이다. 어떤 버튼이 고장났는지 주어졌을 때,
채널 N으로 이동하기 위해서 버튼을 최소 몇 번 눌러야하는지 구하는 프로그램을 작성하시오. 
수빈이가 지금 보고 있는 채널은 100번이다.
"""

# 내 풀이
import sys
from itertools import product
input = sys.stdin.readline
n = int(input()); b = int(input()); s = 100; n_len = len(str(n))
li = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
if b != 0 :
    for i in list(map(int, input().split())) :
        li.remove(i)

if n == s :
    print(0)
elif b == 10 :
    print(abs(n - s))
else :
    check = False
    start = 1
    result = abs(n - s)
    while True :
        com = list(product(li, repeat = start))

        for j in com :
            num = ''
            for k in j :
                num += str(k)
            count = abs(n - int(num)) + len(num)
            if count < result :
                result = count
            else :
                pass
        
        del com
        
        if start + 1 > n_len + 1 :
            break
        else :
            start += 1

    print(result)
    
# Case Study
import sys
input = sys.stdin.readline

def check(num):
    num = list(str(num))
    for i in num:
        if i in s:
            return False
    return True

n = int(input())
m = int(input())
s = list(input().strip())
result = abs(n - 100)

for i in range(1000001):
    if check(i):
        result = min(result, len(str(i)) + abs(i - n))
print(result)

"""
insight 정리
1. 브루트 포스도 이렇게까지 어려워 질 수 있구나를 깨달은 문제.. 한 문제에 이렇게 많이 틀려보기도 처음이다..
2. itertools 참고자료 : https://velog.io/@insutance/Python-순열과-조합-라이브러리
"""