# 1. 2748 - 피보나치 수 2 (https://www.acmicpc.net/problem/2748)
"""
피보나치 수는 0과 1로 시작한다. 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다.
그 다음 2번째 부터는 바로 앞 두 피보나치 수의 합이 된다.
이를 식으로 써보면 Fn = Fn-1 + Fn-2 (n ≥ 2)가 된다.
n=17일때 까지 피보나치 수를 써보면 다음과 같다.
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597
n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.
"""

# # 내 풀이
import sys
n = int(sys.stdin.readline())

def fib(num) :
    if num == 0 :
        return 0
    elif num == 1 :
        return 1
    else :
        return fib(num-1) + fib(num-2)
print(fib(n))

# Case Study
import sys
n = int(sys.stdin.readline())
li = [0] * 91

def fib(num) :
    if num == 0 :
        return 0
    elif num == 1 :
        return 1

    if li[num] != 0 :
        return li[num]
    li[num] = fib(num-1) + fib(num-2)
    return li[num]
print(fib(n))

"""
insight 정리
1. 다이나믹 프로그래밍은 메모리 공간을 약간 더 사용해서 연산 속도를 비약적으로 증가시키는 방법
2. 조건 : 큰 문제를 작은 문제로 나눌 수 있다., 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다.
3. 위의 문제는 단순 재귀함수는 통과되지 않았고, 메모이제이션 기법이 포함된 재귀함수는 통과되었음.
4. 40, 41번 사이에 print(li)를 넣어보면 메모이제이션이 어떻게 적용되고 있는지 확인할 수 있음
"""