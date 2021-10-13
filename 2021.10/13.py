# 1. 1018 - 체스판 다시 칠하기 (https://www.acmicpc.net/problem/1018)
"""
문제 설명
지민이는 자신의 저택에서 MN개의 단위 정사각형으로 나누어져 있는 M*N 크기의 보드를 찾았다.
어떤 정사각형은 검은색으로 칠해져 있고, 나머지는 흰색으로 칠해져 있다.
지민이는 이 보드를 잘라서 8*8 크기의 체스판으로 만들려고 한다.
체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다.
구체적으로, 각 칸이 검은색과 흰색 중 하나로 색칠되어 있고, 변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다.
따라서 이 정의를 따르면 체스판을 색칠하는 경우는 두 가지뿐이다. 하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.
보드가 체스판처럼 칠해져 있다는 보장이 없어서, 지민이는 8*8 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다.
당연히 8*8 크기는 아무데서나 골라도 된다. 지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.
"""

# 내 풀이
import sys
N, M = map(int, sys.stdin.readline().split())
li = []
for _ in range(0, N) :
    chess = input()
    stan = [i for i in chess]
    li.append(stan)

def compare(i, j, li, start) :
    com_w = [['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W']]*4
    com_b = [['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B']]*4
    if start == 'W' :
        com = com_w
    else :
        com = com_b
    count = 0
    for k in range(0,8) :
        for x in range(0,8) :
            if li[i+k][j+x]==com[k][x] :
                pass
            else :
                count+=1
    return count

re = []
for i in range(0, N-7) :
    for j in range(0, M-7) :
        if li[i][j] == 'W' :
            re.append(compare(i,j,li,'W'))
        else :
            re.append(compare(i,j,li,'B'))
        
print(min(re))

# Case Study
N, M = map(int, input().split())
original = []
count = []

for _ in range(N):
    original.append(input())

for a in range(N-7):
    for b in range(M-7):
        index1 = 0
        index2 = 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0:
                    if original[i][j] != 'W':
                        index1 += 1
                    if original[i][j] != 'B':
                        index2 += 1
                else:
                    if original[i][j] != 'B':
                        index1 += 1
                    if original[i][j] != 'W':
                        index2 += 1
        count.append(min(index1, index2))

print(min(count))

"""
insight 정리
1. 문자열은 굳이 split하지 않아도 인덱싱 할 수 있는데 왜 자꾸 split을 하려고 하는가요.. '굳이' 인덱싱을 해서 코드가 많이 늘어났다.
2. 체스판의 원리 -> 체스판의 가로 세로를 x, y 좌표로 나타내었을 때 x+y가 홀수일 경우, 짝수일 경우 각각 같은 색상을 갖는다.
3. 브루트포스 알고리즘은 용어의 뜻 그대로 무식하다. 그러니 코드 짤 때 무식하게 짠거 같은게 정답일 수 있다.
4. 내가 짠 코드가 아직도 왜 틀렸는지 모르겠다.. 
"""

# ----------------------------------------------------------------------------

# 2. 10814 - 나이순 정렬 (https://www.acmicpc.net/problem/10814)
"""
문제 설명
온라인 저지에 가입한 사람들의 나이와 이름이 가입한 순서대로 주어진다.
이때, 회원들을 나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬하는 프로그램을 작성하시오.
"""

# 내 풀이
import sys
N = int(input())
li = [[i] for i in range(1, 201)]
for _ in range(N) :
    a, b = sys.stdin.readline().split()
    li[int(a)-1].append(b)

for i in li :
    if len(i) == 1 :
        pass
    else :
        for j in range(1, len(i)) :
            print(f"{i[0]} {i[j]}")

# Case Study
import sys
n = int(sys.stdin.readline())
member = []
for i in range(n):
    member.append(list(sys.stdin.readline().split()))
member.sort(key = lambda x : int(x[0]))
for i in range(n):
    print(member[i][0], member[i][1])

"""
insight 정리
1. sort에 key값을 lambda로 받아 처리하는 예시 체크
2. 겉으로만 보면 Case Study가 더 빠른 연산을 할 것 같지만, 실제로는 내 풀이가 훨씬 빠른 속도 + 메모리 효율의 결과를 보임
3. 내장 함수는 편하긴 하지만 상황에따라 효율성이 떨어지는 케이스가 있음
"""

# ----------------------------------------------------------------------------
