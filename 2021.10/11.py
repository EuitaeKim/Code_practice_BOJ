# 1. 4299 - AFC 윔블던 (https://www.acmicpc.net/problem/4299)
"""
문제 설명
2012년 12월 2일. 불가능할 것 같았던 사건이 일어났다. 2012-13 FA Cup 2라운드 에서 두 팀이 맞붙게 된 것이었다.
어서 빨리 이 경기를 보고 싶었던 원섭이는 FA Cup을 중계해주는 SBS ESPN의 편성표를 검색해보았다.
하지만, 두 팀간의 경기는 한국인에게 별로 관심을 끌지 못하는 경기였기 때문에, 중계가 예정되어 있지 않았다.
원섭이는 잉글랜드에 거주하는 지수에게 경기 결과를 물어봤다. 지수는 축구에는 큰 관심이 없지만 원섭이를 괴롭히는 것을 좋아하는 친구다.
지수는 두 팀의 최종 점수를 알려주는 대신, 두 팀이 득점한 점수의 합과 차를 알려주었다.
MK 돈스와 AFC 윔블던의 점수의 합과 차가 주어졌을 때, 최종 점수를 구하는 프로그램을 작성하시오.
"""

# 내 풀이
A, B = map(int, input().split())

a = (A + B) / 2
b = (A - B) / 2
if int(a) != a or int(b) != b or a < 0 or b < 0 :
    print(-1)
else :
    if a + b == A and a - b == B :
        print(int(a), int(b))
    else :
        print(-1)

# Case Study
s, m = map(int, input().split())

if  s + m < 0 or s - m < 0 or (s + m) % 2:
    print(-1)
else:
    a = (s + m) // 2
    b = s - a
    print(max(a, b), min(a, b))

"""
insight 정리
1. 예외처리 어렵다. 특히 힌트로 알 수 없는 예외처리를 하는 경우에는 수학적 사고가 이렇게 중요하구나를 몸으로 깨달았다.. ^^
2. 두 팀의 점수와 점수의 합/차에서 발생할 수 있는 모든 예외 케이스를 최대한 찾아보고 코드로 적용 -> 점수의 합/차의 예외처리만으로 예외처리 진행
3. 이미 문제에 두 팀의 점수는 음이 아닌 정수라는 조건이 있었는데 제대로 활용 못하고 a < 0 or b < 0와 같은 코드를 작성했던 점 체크
"""

# ----------------------------------------------------------------------------

# 2. 1259 - 팰린드롬수 (https://www.acmicpc.net/problem/1259)
"""
문제 설명
어떤 단어를 뒤에서부터 읽어도 똑같다면 그 단어를 팰린드롬이라고 한다. 'radar', 'sees'는 팰린드롬이다.
수도 팰린드롬으로 취급할 수 있다. 수의 숫자들을 뒤에서부터 읽어도 같다면 그 수는 팰린드롬수다. 121, 12421 등은 팰린드롬수다.
123, 1231은 뒤에서부터 읽으면 다르므로 팰린드롬수가 아니다. 또한 10도 팰린드롬수가 아닌데, 앞에 무의미한 0이 올 수 있다면
010이 되어 팰린드롬수로 취급할 수도 있지만, 특별히 이번 문제에서는 무의미한 0이 앞에 올 수 없다고 하자.
"""

# 내 풀이
while True :
    a = str(input())
    if int(a) == 0 :
        break

    a_li = [a[i] for i in range(0, len(a))]
    
    while True :
        idx = 0
        if int(a_li[idx]) == 0 :
            del a_li[idx]
            idx += 1
        else :
            break

    a_li_rev = [a_li[i] for i in range(len(a_li) -1, -1, -1)]

    count = 0
    for i in range(0, len(a_li) // 2) :
        if a_li[i] == a_li_rev[i] :
            count += 1
        else :
            print('no')
            break

    if count == len(a_li) // 2 :
        print('yes')

# Case Study
a = list(map(int,input()))

while a != [0] :
  b = list(reversed(a))

  if a == b :
    print("yes")
  else:
    print("no")
  a = list(map(int,input()))

"""
insight 정리
1. 입력값을 받음 -> 숫자로 변환 -> 리스트화 -> [0, 1, 2]과 같이 출력
2. list.sort()처럼 reversed(a)로 리스트 정렬을 변환시킬 수 있다
3. 입력을 굳이 while 안에서 받을 필요없음
"""

# ----------------------------------------------------------------------------

# 3. 2775 - 부녀회장이 될테야 (https://www.acmicpc.net/problem/2775)
"""
문제 설명
평소 반상회에 참석하는 것을 좋아하는 주희는 이번 기회에 부녀회장이 되고 싶어 각 층의 사람들을 불러 모아 반상회를 주최하려고 한다.
이 아파트에 거주를 하려면 조건이 있는데, “a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을
데려와 살아야 한다” 는 계약 조항을 꼭 지키고 들어와야 한다.
아파트에 비어있는 집은 없고 모든 거주민들이 이 계약 조건을 지키고 왔다고 가정했을 때, 주어지는 양의 정수 k와 n에 대해
k층에 n호에는 몇 명이 살고 있는지 출력하라. 단, 아파트에는 0층부터 있고 각층에는 1호부터 있으며, 0층의 i호에는 i명이 산다.
"""

# 내 풀이
li = [[1] for _ in range(0, 14)]

for i in range(2, 15) :
    li[0].append(i)

for j in range(1, 14) :
    for i in range(1, 14) :
        li[j].append(li[j][i-1] + li[j-1][i])

N = int(input())
for _ in range(N) :
    k = int(input())
    n = int(input())
    print(li[k][n-1])

# Case Study
t = int(input())

for _ in range(t) :  
    floor = int(input())
    num = int(input())
    f0 = [x for x in range(1, num+1)]

    for k in range(floor) :
        for i in range(1, num) :
            f0[i] += f0[i-1]

    print(f0[-1])

"""
insight 정리
1. 전체 층, 호수의 위치를 갖는 이중 리스트를 구현한 후 점화식을 활용하여 전체 배열을 생성. 이후 주어진 층, 호의 값을 인덱스로 활용하여 결과 도출
-> 0층에 해당하는 단일 리스트를 구현한 후 주어진 층, 호수만큼의 연산을 진행한 후 단일 리스트에 덮어씌우며 결과를 도출
2. 내가 사용한 방법도 상황에 따라 활용할 수는 있지만, 채점 기준에서는 런타임 에러가 발생 했음
3. 필요한 만큼만 연산을 진행하는 방법 + 단일 리스트만 활용하여 결과를 효율적으로 도출하는 방법 체크해두기
"""