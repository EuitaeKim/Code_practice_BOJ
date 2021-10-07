# 1. 22403 - 阿吽の呼吸 (https://www.acmicpc.net/problem/22403)
"""
문제 설명
외국어여서 생략
"""

# 내 풀이
n = int(input())
count, miss = 0, 0
for _ in range(n) :
    i = input()
    if i == 'A' :
        count += 1

    if i == 'Un' :
        if count != 0 :
            count -= 1
        else :
            miss += 1
            print('NO')
            break

if count == 0 and miss == 0 :
    print('YES')

if count > 0 and miss == 0 :
    print('NO')

"""
insight 정리
"""

# ----------------------------------------------------------------------------

# 2. 3986 - 좋은단어 (https://www.acmicpc.net/problem/3986)
"""
문제 설명
평석이는 단어 위로 아치형 곡선을 그어 같은 글자끼리(A는 A끼리, B는 B끼리) 쌍을 짓기로 하였다.
만약 선끼리 교차하지 않으면서 각 글자를 정확히 한 개의 다른 위치에 있는 같은 글자와 짝 지을수 있다면,
그 단어는 '좋은 단어'이다. 평석이가 '좋은 단어' 개수를 세는 것을 도와주자.
"""

# 내 풀이
N = int(input())
count = 0
for _ in range(N) :
    a = str(input())
    li = []
    for i in a :
        if len(li) == 0 or li[-1] is not i :
            li.append(i)
        else :
            while len(li) != 0 :
                if i == li[-1] :
                    li.pop()
                else :
                    break
    if len(li) == 0 :
        count += 1
print(count)

# Case Study
N = int(input())
answer = 0

for _ in range(N):
    word = input()
    stack = []
    for w in word:
        if stack and stack[-1] == w:
            stack.pop()
        else:
            stack.append(w)
    if not stack:
        answer += 1

print(answer)

"""
insight 정리
"""

# ----------------------------------------------------------------------------

# 3. 문제번호 - 분해합 (https://www.acmicpc.net/problem/2231)
"""
문제 설명
어떤 자연수 N이 있을 때, 그 자연수 N의 분해합은 N과 N을 이루는 각 자리수의 합을 의미한다. 어떤 자연수 M의 분해합이 N인 경우, M을 N의 생성자라 한다.
예를 들어, 245의 분해합은 256(=245+2+4+5)이 된다. 따라서 245는 256의 생성자가 된다.
물론, 어떤 자연수의 경우에는 생성자가 없을 수도 있다. 반대로, 생성자가 여러 개인 자연수도 있을 수 있다.
자연수 N이 주어졌을 때, N의 가장 작은 생성자를 구해내는 프로그램을 작성하시오.
"""

# 내 풀이
def make_list(n_list, N, start = 0) :
    for i in range(start, N) :
        j = str(i)
        j_sum = 0
        for k in j :
            j_sum += int(k)
        n_list[i] = i + j_sum
    return n_list

def fine_index(n_list, N) :
    if n_list.index(N) is not None :
        return n_list.index(N)
    else :
        return 0

N = int(input())
n_list = [0] * N

if len(str(N)) < 3 :
    n_list = make_list(n_list, N)
    print(fine_index(n_list, N))
else :
    n_list = make_list(n_list, N, N - (len(str(N))*9))
    print(fine_index(n_list, N))

# Case Study
N = int(input())
re = 0
for i in range(1, N + 1) :
    A = list(map(int, str(i)))
    re = i + sum(A)
    if re == N :
        print(i)
        break
    if i == N :
        print(0)

"""
insight 정리
"""

# ----------------------------------------------------------------------------

# 4. 2798 - 블랙잭 (https://www.acmicpc.net/problem/2798)
"""
문제 설명
한국 최고의 블랙잭 고수 김정인은 새로운 블랙잭 규칙을 만들어 상근, 창영이와 게임하려고 한다.
김정인 버전의 블랙잭에서 각 카드에는 양의 정수가 쓰여 있다. 그 다음, 딜러는 N장의 카드를 모두 숫자가 보이도록 바닥에 놓는다. 그런 후에 딜러는 숫자 M을 크게 외친다.
이제 플레이어는 제한된 시간 안에 N장의 카드 중에서 3장의 카드를 골라야 한다. 블랙잭 변형 게임이기 때문에, 플레이어가 고른 카드의 합은 M을 넘지 않으면서 M과 최대한 가깝게 만들어야 한다.
N장의 카드에 써져 있는 숫자가 주어졌을 때, M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구해 출력하시오.
"""

# 내 풀이
N, M = map(int, input().split())
n_list = list(map(int, input().split()))
n_list.sort(reverse=True)
sum_list = [1]
for i in n_list :
    for j in n_list[1 : ] :
        for k in n_list[2 : ] :
            n_sum = i + j + k
            if (n_sum <= M) and (i != j) and (j != k) and (k != i) and (n_sum not in sum_list) and (n_sum > max(sum_list)) :
                sum_list.append(n_sum)
            else :
                pass
print(max(sum_list))

# Case Study
mylist=[]
cnt=0

N, M= map(int,input().split())
mylist=list(map(int,input().split()))

for i in range(N):
    for k in range(i+1,N):
        for j in range(k+1,N):
            if mylist[i]+mylist[k]+mylist[j]>M:
                continue
            else:
                cnt=max(cnt,mylist[i]+mylist[k]+mylist[j] )

print(cnt)

"""
insight 정리
"""

# ----------------------------------------------------------------------------

# while True :
#     #a = str(input())
#     a = '[ first in ] ( first out ).'
#     if a == '.' :
#         break

#     stack = []
#     bracket = ["(", "[", "]", ")"]
#     for i in a :
#         if i not in bracket :
#             pass
#         else :
#             if ((len(stack) == 0) and ((i is not  "(") or (i is not "["))) :
#                 print('no')
#                 break
#             else :
#                 if len(stack) == 0 :
#                     stack.append(i)
#                 else :
#                     if not ((stack[-1] == '[' and i == ']') or (stack[-1] == '(' and i == ')')) :
#                         stack.append(i)
#                     else :
#                         while len(stack) != 0 :
#                             if (stack[-1] == '[' and i == ']') or (stack[-1] == '(' and i == ')') :
#                                 stack.pop()
#                                 break
#                             else :
#                                 break
#     if len(stack) == 0 :
#         print('yes')
#     else :
#         print('no')