# 1. 11723 - 집합 (https://www.acmicpc.net/problem/11723)
"""
문제 설명
비어있는 공집합 S가 주어졌을 때, 아래 연산을 수행하는 프로그램을 작성하시오.
add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
all: S를 {1, 2, ..., 20} 으로 바꾼다.
empty: S를 공집합으로 바꾼다. 
"""

# 내 풀이
import sys
n = int(sys.stdin.readline())

li = []
for _ in range(n) :
    com = list(map(str, sys.stdin.readline().split()))
    if com[0] == 'add' :
        if com[1] not in li :
            li.append(com[1])
        else :
            pass
    elif com[0] == 'remove' :
        try :
            li.remove(com[1])
        except :
            pass
    elif com[0] == 'check' :
        if com[1] in li :
            print(1)
        else :
            print(0)
    elif com[0] == 'toggle' :
        if com[1] in li :
            li.remove(com[1])
        else :
            li.append(com[1])
    elif com[0] == 'all' :
        li = [str(i) for i in range(1, 21)]
    elif com[0] == 'empty' :
        li = []

# Case Study
import sys
n = int(sys.stdin.readline())
r = 0

for _ in range(n) :
    com = list(map(str, sys.stdin.readline().split()))
    if com[0] == 'add' :
        r |= 1 << int(com[1])
    elif com[0] == 'remove' :
        r &= ~(1 << int(com[1]))
    elif com[0] == 'check' :
        if r & (1 << int(com[1])) :
            print(1)
        else :
            print(0)
    elif com[0] == 'toggle' :
        r ^= (1 << int(com[1]))
    elif com[0] == 'all' :
        r = (1 << 21) -1
    elif com[0] == 'empty' :
        r = 0

"""
insight 정리
1. 비트마스킹에 대한 개념 이해 및 적용하기.
2. 에라토스테네스의 체를 적용하면서 활용했던 리스트 기반의 기본 연산보다 비용 측면에서 유용함.
3. 따라서 문제의 조건을 보면서 or, and, xor, toggle 등의 기능만 구현하면 된다 싶으면 비트마스킹을 바로 적용해보면 좋을 듯.
"""

# ----------------------------------------------------------------------------

# 2. 1764 - 듣보잡 (https://www.acmicpc.net/problem/1764)
"""
문제 설명
김진영이 듣도 못한 사람의 명단과, 보도 못한 사람의 명단이 주어질 때, 듣도 보도 못한 사람의 명단을 구하는 프로그램을 작성하시오.
첫째 줄에 듣도 못한 사람의 수 N, 보도 못한 사람의 수 M이 주어진다.
이어서 둘째 줄부터 N개의 줄에 걸쳐 듣도 못한 사람의 이름과, N+2째 줄부터 보도 못한 사람의 이름이 순서대로 주어진다.
이름은 띄어쓰기 없이 알파벳 소문자로만 이루어지며, 그 길이는 20 이하이다. N, M은 500,000 이하의 자연수이다.
듣도 못한 사람의 명단에는 중복되는 이름이 없으며, 보도 못한 사람의 명단도 마찬가지이다.
"""

# 내 풀이
import sys
n, m = map(int, sys.stdin.readline().split())
li = [str(sys.stdin.readline().rstrip()) for _ in range(n)]
li.sort()
re = [0] * n

for _ in range(m) :
    b = str(sys.stdin.readline().rstrip())
    try :
        re[li.index(b)] = 1
    except :
        pass

for i, j in zip(li, re) :
    if j == 1 :
        print(i)

# Case Study
import sys
n, m = map(int, sys.stdin.readline().split())
li = [str(sys.stdin.readline().rstrip()) for _ in range(n+m)]
li.sort()
re = []
i = 0
while i < n + m - 1 :
    if li[i] == li[i+1] :
        re.append(li[i])
        i += 2
    else :
        i += 1
print(len(re))
for i in re :
    print(i)

"""
insight 정리
1. 50만개의 이름을 담은 리스트 생성 + 정렬 + 50만개의 인덱스를 담은 리스트 생성 + 50만개의 이름을 하나씩 받으면서 중복 일 경우 그 단어의 인덱스 값을 변경 ->
100만개 이름을 담은 리스트 생성 + 정렬 + 처음부터 순서대로 비교 진행
2. 내 방법은 시간초과, Case Study는 통과함. 내 방식이 더 효율적일 것으로 생각했지만, 코드를 뜯어보니 다루는 데이터가 훨씬 많아짐
3. 약간 괜히 어렵게 생각했다가 더 어려워진 케이스. 단순히 데이터를 다 받아와서 연산하는 것은 함정이라고 생각했는데 그게 정답이었다..
"""

# ----------------------------------------------------------------------------
