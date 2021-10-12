# 1. 2839 - 설탕 배달 (https://www.acmicpc.net/problem/2839)
"""
문제 설명
상근이는 요즘 설탕공장에서 설탕을 배달하고 있다. 상근이는 지금 사탕가게에 설탕을 정확하게 N킬로그램을 배달해야 한다.
설탕공장에서 만드는 설탕은 봉지에 담겨져 있다. 봉지는 3킬로그램 봉지와 5킬로그램 봉지가 있다.
상근이는 귀찮기 때문에, 최대한 적은 봉지를 들고 가려고 한다. 예를 들어, 18킬로그램 설탕을 배달해야 할 때,
3킬로그램 봉지 6개를 가져가도 되지만, 5킬로그램 3개와 3킬로그램 1개를 배달하면, 더 적은 개수의 봉지를 배달할 수 있다.
상근이가 설탕을 정확하게 N킬로그램 배달해야 할 때, 봉지 몇 개를 가져가면 되는지 그 수를 구하는 프로그램을 작성하시오.
"""

# 내 풀이
N = int(input())

kg5 = N // 5

while kg5 >= 0 :
    diff = N - (5 * kg5)
    kg3 = diff // 3
    diff -= 3 * kg3
    if diff == 0 :
        print(kg3 + kg5)
        break
    else :
        kg5 -= 1

if kg5 < 0 :
    print(-1)

# Case Study
a = int(input())
k = a // 5
while k >= 0:
    if ((a - k * 5) / 3).is_integer():
        break
    k -= 1
print((k + (a - k * 5) // 3) if k >= 0 else -1)

"""
insight 정리
1. 이렇게까지 간단하게 풀어낼 수 있구나라는 점을 체크해두기
2. 내가 작성하는 코드는 대체로 세부 스텝을 한 줄씩 모두 구현하는 느낌. Case 코드처럼 필요한 부분만 딱 짚어서 코드짜는 스킬을 길러야 할 듯
"""

# ----------------------------------------------------------------------------

# 2. 1436 - 영화감독 숌 (https://www.acmicpc.net/problem/1436)
"""
문제 설명
종말의 숫자란 어떤 수에 6이 적어도 3개이상 연속으로 들어가는 수를 말한다.
제일 작은 종말의 숫자는 666이고, 그 다음으로 큰 수는 1666, 2666, 3666, .... 과 같다.
따라서, 숌은 첫 번째 영화의 제목은 세상의 종말 666, 두 번째 영화의 제목은 세상의 종말 1666 이렇게 이름을 지을 것이다.
일반화해서 생각하면, N번째 영화의 제목은 세상의 종말 (N번째로 작은 종말의 숫자) 와 같다.
숌이 만든 N번째 영화의 제목에 들어간 숫자를 출력하는 프로그램을 작성하시오.
숌은 이 시리즈를 항상 차례대로 만들고, 다른 영화는 만들지 않는다.
"""

# 내 풀이
start = str(666)
li = []
for i in range(0, 10) :
    for j in range(0, 10) :
        for k in range(0, 10) :
            for x in range(0, 10) :
                li.append(int(str(i) + str(j) + str(k) + str(x) + start))
                li.append(int(str(i) + str(j) + str(k) + start + str(x)))
                li.append(int(str(i) + str(j) + start + str(k) + str(x)))
                li.append(int(str(i) + start + str(j) + str(k) + str(x)))
                li.append(int(start + str(i) + str(j) + str(k) + str(x)))

li = list(set(li))
li.sort()
N = int(input())
print(li[N-1])

# Case Study
n=int(input())
i=0
while n:
    i+=1
    if "666" in str(i):
        n-=1
print(i)

"""
insight 정리
1. 브루트포스 알고리즘이 왜 브루트포스라고 명명되었는지 몸소 깨달았다 ^^..
2. Case : 숫자로 +1 씩 증가시키고, 문자로 666이 있는지 검토한다. 또한 리스트를 만들어 인덱스를 활용하지 않고,
주어진 n번째 수를 하나씩 -1 함으로써 리스트를 굳이 생성하지 않고 결과를 출력한다.
"""

# ----------------------------------------------------------------------------

# 3. 2609 - 최대공약수와 최소공배수 (https://www.acmicpc.net/problem/2609)
"""
문제 설명
두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.
"""

# 내 풀이
A,B=map(int,input().split())
li=[i for i in range(1, max(A,B)+1) if A%i==0 and B%i==0]
re=max(li)
print(f"{re}\n{(A)*(B//re)}")

# Case Study
import math
x, y = map(int, input().split())

print(math.gcd(x, y))
print(math.lcm(x, y))

"""
insight 정리
1. 갓이썬은 역시나 최대공약수, 최소공배수를 계산하는 math 함수를 가지고 있었다.
"""

# ----------------------------------------------------------------------------

# 4. 2751 - 수 정렬하기 2 (https://www.acmicpc.net/problem/2751)
"""
문제 설명
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
"""

# 내 풀이
N = int(input())
li = [int(input()) for _ in range(N)]
li.sort()
for i in range(N) :
    print(li[i])

# Case Study
import sys
n = int(input())
l = []
for i in range(n) :
    l.append(int(sys.stdin.readline()))
for i in sorted(l) :
    sys.stdout.write(str(i)+'\n')

"""
insight 정리
1. 앞으로도 백준에서 자주 겪게 될 문제 중 하나로, 정확한 정답을 도출하지만 시간 제한에 걸리게 되는 경우를 주의할 것
2. 내 풀이는 실패, Case Study는 성공했는데 이유 : input() 내장 함수는 sys.stdin.readline()과 비교해서 prompt message를 출력하고,
개행 문자를 삭제한 값을 리턴하기 때문에 느리다 (참고 : https://buyandpray.tistory.com/7)
"""