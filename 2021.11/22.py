# 1. 1934 - 최소공배수 (https://www.acmicpc.net/problem/1934)
"""
문제 설명
두 자연수 A와 B에 대해서, A의 배수이면서 B의 배수인 자연수를 A와 B의 공배수라고 한다.
이런 공배수 중에서 가장 작은 수를 최소공배수라고 한다.
예를 들어, 6과 15의 공배수는 30, 60, 90등이 있으며, 최소 공배수는 30이다.
두 자연수 A와 B가 주어졌을 때, A와 B의 최소공배수를 구하는 프로그램을 작성하시오.
"""

# 내 풀이
import sys
li = [0 for _ in range(45001)]
for i in range(2, 45001) :
    if li[i] == 0 :
        for j in range(i, 45001, i) :
            li[j] = 1
        if i != 2 :
            li[i] = 2

for _ in range(int(sys.stdin.readline())) :
    a, b = map(int, sys.stdin.readline().split())
    if li[a] == 2 or li[b] == 2 :
        print(a*b)
    elif a == 1 or b == 1 :
        print(a*b)
    else :
        ma = max(a, b)
        result = 1
        while True :
            for i in range(2, ma + 1) : 
                if a%i == 0 and b%i == 0 :
                    result *= i
                    a = a//i
                    b = b//i
                    ma = max(a, b)
                    break
            break
        print(result * a * b)

# Case Study
T = int(input())

def GCD(x, y):
  x, y = min(x, y), max(x, y)
  while x != 0:
    (x, y) = (y % x, x)
  return y

for _ in range(T):
  a, b = map(int, input().split())
  a, b = min(a, b), max(a, b)
  g = GCD(a, b)
  result = a * b // g
  print(result) 

"""
insight 정리
- 최대공약수 : Greatest Common Divisor -> 두 수 혹은 그 이상의 수들의 공통인 약수 중 최대인 것
- 최소공배수 : Largest Common Multiple -> 두 수 혹은 그 이상의 수들의 공통인 배수 중 최소인 것
- 유클리드 호제법 : x, y의 최대공약수는 y, r(x%y)의 최대공약수와 같다.
- 기본적으로 최대공약수를 구할 수 있다면 최소공배수는 쉽게 구할 수 있다는 것을 이해해야 한다.
- 이를테면 a, b가 있고 두 수의 최대공약수가 c라면, a*b는 c^2*d로 이루어져 있으며, 이 값을 c로 나누면 나오는 값이 최소공배수가 된다.
- 이때 최대공약수를 구하기 위해 알고리즘에서 자주 사용되는 것이 유클리드 호제법이다.
- 결론은 수학 공부를 안했더니 코드가 쓸데없이 길어졌다는 것.. 또한 갓이썬은 math.gcd, math.lcm으로 간편하게 구할 수 있다는 것.. 또한 나는
이 내용을 이전에 다룬적이 있었는데, 그새 까먹었다는 것..
"""