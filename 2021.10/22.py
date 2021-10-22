# 1. 1920 - 수 찾기 (https://www.acmicpc.net/problem/1920)
"""
문제 설명
N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.
"""

# 내 풀이
import sys
a = int(input())
li_1 = list(map(int, sys.stdin.readline().split()))
b = int(input())
li_2 = list(map(int, sys.stdin.readline().split()))

li_1.sort()
for i in li_2 :
    start, end, mid = 0, a-1, a//2
    while start != end :
        if i == li_1[mid] or i == li_1[start] or i == li_1[end] :
            print(1)
            break
        elif i > li_1[mid] :
            start = mid + 1
            mid = abs((end + start))//2
            if start == end :
                print(0)
                break
        else :
            end = mid - 1
            mid = abs((end - start))//2
            if start == end :
                print(0)
                break

# Case Study
from sys import stdin, stdout
n = stdin.readline()
N = sorted(map(int,stdin.readline().split()))
m = stdin.readline()
M = map(int, stdin.readline().split())

def binary(l, N, start, end):
    if start > end:
        return 0
    m = (start+end)//2
    if l == N[m]:
        return 1
    elif l < N[m]:
        return binary(l, N, start, m-1)
    else:
        return binary(l, N, m+1, end)

for l in M:
    start = 0
    end = len(N)-1
    print(binary(l,N,start,end))

# Case Study
from sys import stdin, stdout
n = stdin.readline()
N = set(stdin.readline().split())
m = stdin.readline()
M = stdin.readline().split()

for l in M:
    stdout.write('1\n') if l in N else stdout.write('0\n')

"""
insight 정리
1. 정답은 나오지만 시간 초과로 실패가 뜨는 경우 -> 재귀를 활용해 문제를 해결한 경우
2. 이분 탐색의 경우 중간 값이 오른쪽이든 왼쪽이든, 업데이트를 할 때 (start+end)//2로 간단하게 업데이트할 수 있었음.
-> 근데 나는 굳이 그 경우를 쪼갬으로써 코드를 굳이굳이 늘림
3. https://chancoding.tistory.com/44 링크에서 설명하는 시간 복잡도 개념 이해 및 숙지하기
4. input()에 들어오는 값이 엄청나게 많아지면 input()과 sys.stdin.readline()의 속도 차이가 엄청 커진다.
"""

# ----------------------------------------------------------------------------

# 2. 2164 - 카드2 (https://www.acmicpc.net/problem/2164)
"""
문제 설명
N장의 카드가 있다. 각각의 카드는 차례로 1부터 N까지의 번호가 붙어 있으며,
1번 카드가 제일 위에, N번 카드가 제일 아래인 상태로 순서대로 카드가 놓여 있다.
이제 다음과 같은 동작을 카드가 한 장 남을 때까지 반복하게 된다. 우선, 제일 위에 있는 카드를 바닥에 버린다.
그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.
N이 주어졌을 때, 제일 마지막에 남게 되는 카드를 구하는 프로그램을 작성하시오.
"""

# 내 풀이
n = int(input())
li = [i for i in range(1, n+1)]
while len(li) != 1 :
    li.pop(0)
    li.append(li.pop(0))

print(li[0])

# Case Study
from collections import deque
N = int(input())
deque = deque([i for i in range(1, N+1)])
while(len(deque) >1):
    deque.popleft()
    move_num = deque.popleft()
    deque.append(move_num)

print(deque[0])

"""
insight 정리
1. 직접 구현으로 시간 초과가 뜨는 경우 파이썬 라이브러리 활용을 고민해 볼 것
2. 내 풀이와 Case Study를 보면 형태는 거의 비슷한데 내 코드는 시간 초과가 뜨고, Case Study는 통과되는 모습을 볼 수 있음
3. https://tooo1.tistory.com/88 링크에서 소개하는 출력값의 규칙 발견을 통한 해결 케이스도 종종 확인하자.
"""

# ----------------------------------------------------------------------------

# 3. 11866 - 요세푸스 문제 0 (https://www.acmicpc.net/problem/11866)
"""
문제 설명
요세푸스 문제는 다음과 같다.
1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다.
이제 순서대로 K번째 사람을 제거한다. 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다.
이 과정은 N명의 사람이 모두 제거될 때까지 계속된다. 원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다.
예를 들어 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.
N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오.
"""

# 내 풀이
a, b = map(int, input().split())
li = [i for i in range(1, a+1, 1)]
result = []
start = b - 1
while True :
    result.append(li.pop(start))
    start += b - 1
    if start > len(li) -1 :
        if len(li) == 0 :
            break
        elif len(li) == 1 :
            result.append(li[0])
            break
        else :
            start = start % len(li)

print(str(result).replace('[', '<').replace(']', '>'))

# Case Study
n,k = map(int, input().split())
arr = [i for i in range(1,n+1)]
ans = []
p = 0
while arr:
    p = (p+k-1)%len(arr)
    ans.append(arr.pop(p))
print("<", end="")
print(*ans, sep=", ", end="")
print(">")

"""
insight 정리
1. 굳이굳이굳이굳이 예외처리 해야 할 것을 굳이굳이굳이 찾아 적용한 코드 -> 문제 풀이의 핵심이었던 인덱스 지정을 정확히 활용한 코드
2. 인덱스 활용에 대한 이해가 부족했던 만큼 내 코드의 길이는 늘어났음. 구성 로직과 코드에 대한 명확한 이해를 하면서 작업하자
3. while arr:로 설정함으로써 len(arr) == 0이 되면 중지되도록 설정한 부분 체크하기
"""

# ----------------------------------------------------------------------------