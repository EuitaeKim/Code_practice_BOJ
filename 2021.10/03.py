# 1. 8958 - OX퀴즈 (https://www.acmicpc.net/problem/8958)
"""
문제
"OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다.
O는 문제를 맞은 것이고, X는 문제를 틀린 것이다.
문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다.
예를 들어, 10번 문제의 점수는 3이 된다.
"OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.
OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.
"""
# 내 풀이
N = int(input())

for _ in range(0, N) :
    T = input()
    result = [1 if i == "O" else 0 for i in T]

    for i in range(1, len(result)) :
        if result[i] == 1 and result[i - 1] >= 1 :
            result[i] += result[i - 1]

    final = 0
    for i in result :
        final += i

    print(final)

# Case Study
for i in range(int(input())):
    sum = 0
    cnt = 0
    for i in list(input()):
        if i == 'O':
            sum += 1
            cnt += sum
        else:
            sum = 0
    print(cnt)

"""
insight
1. Case는 X값을 sum을 초기화 시키는데 활용함으로써 효율적으로 코드 작성
2. 리스트를 직접 구해서 결과를 내는 방식 -> input으로 가져올 때 리스트화 시킬 수 있음
3. 총 합을 따로 구하는 방식 -> input으로 들어온 문자를 하나씩 검토하면서 바로 총 합을 계산할 수 있음
"""

# ----------------------------------------------------------------------------

# 2. 10869 - 사칙연산 (https://www.acmicpc.net/problem/10869)
"""
문제
두 자연수 A와 B가 주어진다.
이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오. 
"""
# 내 풀이
a, b = map(int, input())
print(f"{a+b}\n{a-b}\n{a*b}\n{a//b}\n{a%b}")

"""
insight
1. print할 때 \n 을 유연하게 쓸 수 있다는 것만 짚고가기
"""

# ----------------------------------------------------------------------------

# 3. 10952 - A+B - 5 (https://www.acmicpc.net/problem/10952)
"""
문제
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
입력의 마지막에는 0 두 개가 들어온다.
"""
# 내 풀이
while True :
    try :
        a, b = map(int, input().split())
        if a == 0 and b == 0 :
            break
        else :
            print(a+b)
    except :
        break

# Case Study
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    print(a + b)

"""
insight
1. try를 굳이? 굳이 try 쓰느라 코드가 불필요하게 늘어남 -> try를 꼭 쓰지 않아도 되는 상황이었음
"""

# ----------------------------------------------------------------------------

# 4. 11720 - 숫자의 합 (https://www.acmicpc.net/problem/11720)
"""
문제
N개의 숫자가 공백 없이 쓰여있다.
이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.
"""
# 내 풀이
N = int(input())
num = input()
result = 0
for i in num :
    result += int(i)
print(result)

# Case Study
a = int(input())
num = input()
print(sum(list(map(int, str(num)))))

"""
insight
1. N을 안쓸껀데 굳이 int()를 넣을 필요는 없었다. (생각없이 코딩하지 말기)
2. num을 불러와서 문자화키고 이를 반복문을 돌려 result를 출력 -> 반복문없이 map, list, sum을 활용하여 한 줄로 결과를 출력
"""
