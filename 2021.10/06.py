# 1. 17608 - 막대기 (https://www.acmicpc.net/problem/17608)
"""
문제 설명
높이만 다르고 (같은 높이의 막대기가 있을 수 있음) 모양이 같은 막대기를 일렬로 세운 후, 왼쪽부터 차례로 번호를 붙인다.
각 막대기의 높이는 그림에서 보인 것처럼 순서대로 6, 9, 7, 6, 4, 6 이다. 일렬로 세워진 막대기를 오른쪽에서 보면 보이는
막대기가 있고 보이지 않는 막대기가 있다. 즉, 지금 보이는 막대기보다 뒤에 있고 높이가 높은 것이 보이게 된다.
N개의 막대기에 대한 높이 정보가 주어질 때, 오른쪽에서 보아서 몇 개가 보이는지를 알아내는 프로그램을 작성하려고 한다.
"""

# 내 풀이
N = int(input())
N_list = []
for _ in range(N) :
    b = int(input())
    N_list.append(b)

final = []
while len(N_list) != 0 :
    ind = N_list.index(max(N_list))
    final.append(N_list[ind])
    N_list = N_list[ind + 1 : len(N_list)]

# Case Study
print(len(set(final)))

import sys
N = int(sys.stdin.readline())
stack = []
result = 1

for _ in range(N) :
    stack.append(int(sys.stdin.readline()))

Max = stack[-1]
for i in range(len(stack) - 1, - 1, - 1) :
    if stack[i] > Max :
        result += 1
        Max = stack[i]

print(result)

"""
insight 정리
1. 우선 리스트를 받음. 리스트의 최대값의 왼쪽 막대기들은 보이지 않으므로, 최대값 포함 리스트 왼쪽 영역값 삭제 및 최대값 따로 저장 (while 문)
이후 최종 결과는 따로 저장한 리스트의 set 적용 후 길이 출력 -> 자료 탐색을 오른쪽부터 한 것이 핵심. 오른쪽부터 하면 최대값을 더욱 유용하게 사용할 수 있었다.
2. 스택을 꼭 왼쪽 데이터부터 적용 할 필요는 없다. (고정관념 버려!)
"""

# ----------------------------------------------------------------------------

# 2. 1158 - 요세푸스 문제 (https://www.acmicpc.net/problem/1158)
"""
문제 설명
1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다. 이제 순서대로 K번째 사람을 제거한다.
한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다. 이 과정은 N명의 사람이 모두 제거될 때까지 계속된다.
원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다. 예를 들어 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.
N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오.
"""

# 내 풀이
n, k = map(int, input().split())
n_list = [i for i in range(1, n+1)]

num = k - 1
final = []

while len(final) != n :
    final.append(n_list[num])
    n_list.remove(n_list[num])
    num += k - 1
    if num >= len(n_list) and len(n_list) != 0 :
        num = num % len(n_list)

final_2 = ''
for i in final :
    final_2 += str(i) + ', '

print(f"<{final_2[:-2]}>")

# Case Study
N, K = map(int, input().split())
queue = [i for i in range(1, N+1)]

idx = K-1
list1 = []
while queue:
    if idx <= len(queue)-1 :
        list1.append(queue.pop(idx))
        idx += K-1
    else:
        idx = idx % len(queue)
        list1.append(queue.pop(idx))
        idx += K-1

print('<', end='')
for n in list1[:-1]:
    print(n, end=', ')
print(list1[-1], end='')
print('>')

"""
insight 정리
1. 문제는 맞았는데 while 문 안의 세부 동작 로직이 잘 이해가 되지 않아 기록
2. 기존 리스트에서 특정 값을 빼서 다른 리스트에 넣는 경우 pop()을 적극적으로 활용하자. (pop을 안쓰니 코드가 1줄로 될 걸 2줄로 늘어남)
"""

# ----------------------------------------------------------------------------

# 3. 1550 - 16진수 (https://www.acmicpc.net/problem/1550)
"""
문제 설명
16진수 수를 입력받아서 10진수로 출력하는 프로그램을 작성하시오.
"""

# 내 풀이
print(int(input(), 16))

"""
insight 정리
1. 내장함수 int()를 이용해서 숫자나 문자열을 정수형 (Integer)으로 변환하는데, 정수로 변환할 값과 밑을 int(value, base)의 형태로 입력한다. (밑 = 진수)
2. value는 0, base는 10이 디폴트이며, base에 2에서 36 사이의 값을 입력할 수 있다.
"""

# ----------------------------------------------------------------------------