# 1. 4949 - 균형잡힌 세상 (https://www.acmicpc.net/problem/4949)
"""
문제 설명
세계는 균형이 잘 잡혀있어야 한다. 양과 음, 빛과 어둠 그리고 왼쪽 괄호와 오른쪽 괄호처럼 말이다.
정민이의 임무는 어떤 문자열이 주어졌을 때, 괄호들의 균형이 잘 맞춰져 있는지 판단하는 프로그램을 짜는 것이다.
문자열에 포함되는 괄호는 소괄호("()") 와 대괄호("[]")로 2종류이고, 문자열이 균형을 이루는 조건은 아래와 같다.

모든 왼쪽 소괄호("(")는 오른쪽 소괄호(")")와만 짝을 이뤄야 한다.
모든 왼쪽 대괄호("[")는 오른쪽 대괄호("]")와만 짝을 이뤄야 한다.
모든 오른쪽 괄호들은 자신과 짝을 이룰 수 있는 왼쪽 괄호가 존재한다.
모든 괄호들의 짝은 1:1 매칭만 가능하다. 즉, 괄호 하나가 둘 이상의 괄호와 짝지어지지 않는다.
짝을 이루는 두 괄호가 있을 때, 그 사이에 있는 문자열도 균형이 잡혀야 한다.
정민이를 도와 문자열이 주어졌을 때 균형잡힌 문자열인지 아닌지를 판단해보자.
"""

# 내 풀이
import sys
while True :
    a = str(sys.stdin.readline().rstrip())
    li = ['(',')','[',']']
    result = ''
    if a == '.' :
        break

    for i in a :
        if i in li :
            result += i

    if len(result) % 2 != 0 :
        print('no')
    else :
        while True :
            result = result.replace('[]', '').replace('()', '')
            if len(result) == 0 :
                print('yes')
                break
            elif result == result.replace('[]', '').replace('()', '') :
                print('no')
                break

# Case Study
while True :
    s = input()
    if s == '.' :
        break
    li = []
    temp = True
    for i in s :
        if i == '(' or i == '[' :
            li.append(i)
        elif i == ')' :
            if not li or li[-1] == '[' :
                temp = False
                break
            elif li[-1] == '(' :
                li.pop()
        elif i == ']' :
            if not li or li[-1] == '(' :
                temp = False
                break
            elif li[-1] == '[' :
                li.pop()
    
    if temp == True and not li :
        print('yes')
    else :
        print('no')

"""
insight 정리
1. '내 풀이'를 기반으로 문제를 풀 때, '.' 판단을 통한 while문 탈출이 되지 않았음. 그래서 찾아보니, readline()이 오른쪽 공백까지 가져오는게 원인이었음
-> 이번처럼 코드상에 문제가 없는데 탈출이 안되는 경우 입력값 형태를 살펴볼 것 (이거 알아내느라 1시간 걸림..)
2. 이번에 스택 구현, replace 활용 두개 다 해봤는데 replace가 성능이 훨씬 좋았음을 참고하기
3. 스택 구현할 때 temp를 설정함으로써 yes/no의 판단 기준을 명확하게 잡아주는 부분 체크해놓기
"""