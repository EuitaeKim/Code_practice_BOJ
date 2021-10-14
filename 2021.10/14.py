# 1. 10179 - 쿠폰 (https://www.acmicpc.net/problem/10179)
"""
문제 설명
당신은 어떤 물건이라도 20% 할인해주는 쿠폰을 가지고 있다.
원래 가격이 주어질 때, 쿠폰을 사용하면 얼마가 되는지 알려주는 프로그램을 작성하시오.
"""

# 내 풀이
n = int(input())
for _ in range(n) :
    print("${:.2f}".format(float(input())*0.8))

"""
insight 정리
1. 0으로 끝나는 소수를 의도적으로 추가할 수 있는 방법.
"""