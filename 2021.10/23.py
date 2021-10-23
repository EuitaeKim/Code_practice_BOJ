# 1. 1978 - 소수 찾기 (https://www.acmicpc.net/problem/1978)
"""
문제 설명
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.
"""

# 내 풀이
import sys

k = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))

def prime_list(n):
    sieve = [True] * n

    m = int(n ** 0.5)
    for i in range(2, m + 1) :
        if sieve[i] == True :
            for j in range(i + i, n, i) : 
                sieve[j] = False
    return [i for i in range(2, n) if sieve[i] == True]

std = prime_list(1000)
count = 0
for i in li :
    if i in std :
        count += 1

print(count)

"""
insight 정리
1. 에라토스테네스의 체 이론을 활용한 문제 풀이. 앞으로 자주 사용하게 될 것 같아서 기입해두기
"""

# ----------------------------------------------------------------------------

# 2. 10816 - 숫자 카드 2 (https://www.acmicpc.net/problem/10816)
"""
문제 설명
숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다.
정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는 프로그램을 작성하시오.
"""

# 내 풀이
import sys

n = int(sys.stdin.readline())
li_1 = list(map(str, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
li_2 = list(map(str, sys.stdin.readline().split()))

li_1.sort()
dic_li = {}
for i in li_1 :
    if i not in dic_li.keys() :
        dic_li[i] = 1
    else :
        dic_li[i] += 1

result = ''
for i in li_2 :
    if i in dic_li.keys() :
        result += str(dic_li[i]) + ' '
    else :
        result += '0 '

print(result.rstrip())

# Case Study
from collections import defaultdict, Counter
import sys

N = int(sys.stdin.readline())
cards = Counter(sys.stdin.readline().split())
M = int(sys.stdin.readline())
print(*[cards[num] for num in sys.stdin.readline().split()])

"""
insight 정리
1. 갓이썬은 역시 데이터 별 개수를 세어주는 패키지도 제공하고 있었다. 나는 그걸 찾아볼 생각을 하지 않고 '직접' 구현했다 ^^
2. Counter 클래스 활용 기억하고 있기. 그리고 개수 카운트는 리스트보다 딕셔너리를 먼저 생각하기. keys() 적극 활용하기. key는 문자로하기
"""

# ----------------------------------------------------------------------------