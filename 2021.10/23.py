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

# 3. 10989 - 수 정렬하기 3 (https://www.acmicpc.net/problem/10989)
"""
문제 설명
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
"""

# 내 풀이
import sys
n = int(sys.stdin.readline())

li = [0] * 10001
for _ in range(n) :
    a = int(sys.stdin.readline())
    li[a] = li[a] + 1

for i in range(10001) :
    if li[i] != 0 :
        for _ in range(li[i]) :
            print(i)

"""
insight 정리
1. 시간, 메모리 제한이 있는 경우 Counter, Sort 등의 기능이 실패하는 경우가 있음. 이때 활용하는 알고리즘이 Counting sort.
2. 입력으로 들어올 수 있는 데이터의 종류가 10001 종류 라는 점을 이용해서 특정 데이터가 몇 회 등장했는가를 세는 식으로 정렬을 구현한다.
-> 이 방법의 시간복잡도는 O(n)으로, 일반적인 정렬(ex: sorted)의 시간복잡도 O(nlogn)보다 작다.
"""
