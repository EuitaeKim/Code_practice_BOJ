# 1. 2884 - 알람 시계 (https://www.acmicpc.net/problem/2884)
"""
문제
상근이는 매일 아침 알람을 듣고 일어난다. 알람을 듣고 바로 일어나면 다행이겠지만,
항상 조금만 더 자려는 마음 때문에 매일 학교를 지각하고 있다.
상근이는 모든 방법을 동원해보았지만, 조금만 더 자려는 마음은 그 어떤 것도 없앨 수가 없었다.
이런 상근이를 불쌍하게 보던, 창영이는 자신이 사용하는 방법을 추천해 주었다.
바로 "45분 일찍 알람 설정하기"이다.
이 방법은 단순하다. 원래 설정되어 있는 알람을 45분 앞서는 시간으로 바꾸는 것이다.
어차피 알람 소리를 들으면, 알람을 끄고 조금 더 잘 것이기 때문이다. 이 방법을 사용하면,
매일 아침 더 잤다는 기분을 느낄 수 있고, 학교도 지각하지 않게 된다.
현재 상근이가 설정한 알람 시각이 주어졌을 때, 창영이의 방법을 사용한다면,
이를 언제로 고쳐야 하는지 구하는 프로그램을 작성하시오.
"""

# 내 풀이
H, M = map(int, input().split())
if M - 45 < 0 :
    if H - 1 < 0 :
        print(f"{H+23} {M+15}")
    else :
        print(f"{H-1} {M+15}")
else :
    print(f"{H} {M-45}")

# Case Study
H, M = map(int,input().split())
if M >= 45:
  print(H, M - 45)
elif M < 45 and H == 0:
  print(23, M + 15)
else:
  print(H - 1, M + 15)

"""
insight
1. 첫 depth의 if 문에서 M으로 조건을 구분하고 안에 두번째 depth의 if 문을 추가하여 H를 구분(이중 조건)
-> M과 H를 같이 첫 depth의 if 문에서 조건으로 활용하여 간단하게 구분(단일 조건)
2. 큰 task를 작은 task로 쪼갤 때 M H를 굳이 따로 생각해서 쪼갤 필요 없음 (오히려 시간 복잡도가 더 증가할 수 있음)
"""

# ----------------------------------------------------------------------------

# 2. 2908 - 상수 (https://www.acmicpc.net/problem/2908)
"""
문제 설명
상근이의 동생 상수는 수학을 정말 못한다. 상수는 숫자를 읽는데 문제가 있다.
이렇게 수학을 못하는 상수를 위해서 상근이는 수의 크기를 비교하는 문제를 내주었다.
상근이는 세 자리 수 두 개를 칠판에 써주었다. 그 다음에 크기가 큰 수를 말해보라고 했다.
상수는 수를 다른 사람과 다르게 거꾸로 읽는다. 예를 들어, 734와 893을 칠판에 적었다면,
상수는 이 수를 437과 398로 읽는다. 따라서, 상수는 두 수중 큰 수인 437을 큰 수라고 말할 것이다.
두 수가 주어졌을 때, 상수의 대답을 출력하는 프로그램을 작성하시오.
"""

# 내 풀이
a, b = input().split()

def reverse(num, re_num = '') :
    for i in range(len(num)-1, -1, -1) :
        re_num += num[i]
    return int(re_num)

print(max(reverse(a), reverse(b)))

# Case Study
a, b = input().split()
a = int(a[::-1])
b = int(b[::-1])

if (a < b) :
    print(b)
else :
    print(a)

"""
insight 정리
1. 앞으로 숫자 뒤집을때는 굳이 함수까지 만들지 말고 [::-1] 사용하자..
"""

# ----------------------------------------------------------------------------

# 3. 10809 - 알파벳 찾기 (https://www.acmicpc.net/problem/10809)
"""
문제 설명
알파벳 소문자로만 이루어진 단어 S가 주어진다.
각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를,
포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.
"""

# 내 풀이
import string

a = str(input())
check_list = string.ascii_lowercase
fin_list = ''

for i in check_list :
    try :
        fin_list += str(a.index(i)) + ' '
    except :
        fin_list += '-1' + ' '

print(fin_list[:-1])

# Case Study
string = input()
for i in range(97, 123):
		print(string.find(chr(i)), end=" ")

"""
insight 정리
1. 영어 소문자 리스트를 받아 각 문자가 단어에 포함되어 있는지를 확인 + index method
    -> 영어 소문자 범위의 아스키 코드를 활용해 각 문자가 단어에 포함되어 있는지를 확인 + find method
2. find method가 찾는 문자가 없을 때 -1를 리턴한다는 걸 이전에 본적 있었는데 문제로 마주했을 때 활용하지 못함
3. find를 쓰지 않음으로써 try/except가 들어가버린 점 체크해두기
"""

# ----------------------------------------------------------------------------

# 4. 1181 - 단어 정렬 (https://www.acmicpc.net/problem/1181)
"""
문제 설명
알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.
1. 길이가 짧은 것부터
2. 길이가 같으면 사전 순으로
"""

# 내 풀이
N = int(input())
w_list = list(set([input() for _ in range(N)]))
w_list.sort()
w_list.sort(key=len)

for i in w_list :
    print(i)

"""
insight 정리
1. 내장 함수가 분명히 있는데 굳이 반복, 조건문 쓰다간 개미 지옥에 빠질 수 있음을 주의하자
"""

# ----------------------------------------------------------------------------

# 5. 1654 - 랜선 자르기 (https://www.acmicpc.net/problem/1654)
"""
문제 설명
이미 오영식은 자체적으로 K개의 랜선을 가지고 있다. 그러나 K개의 랜선은 길이가 제각각이다.
박성원은 랜선을 모두 N개의 같은 길이의 랜선으로 만들고 싶었기 때문에 K개의 랜선을 잘라서 만들어야 한다.
예를 들어 300cm 짜리 랜선에서 140cm 짜리 랜선을 두 개 잘라내면 20cm는 버려야 한다. (이미 자른 랜선은 붙일 수 없다.)

편의를 위해 랜선을 자르거나 만들 때 손실되는 길이는 없다고 가정하며, 기존의 K개의 랜선으로 N개의 랜선을 만들 수 없는 경우는 없다고 가정하자.
그리고 자를 때는 항상 센티미터 단위로 정수길이만큼 자른다고 가정하자. N개보다 많이 만드는 것도 N개를 만드는 것에 포함된다.
이때 만들 수 있는 최대 랜선의 길이를 구하는 프로그램을 작성하시오.
"""

# 내 풀이 (오답)
K, N = map(int, input().split())
line_list = []
line_sum = 0
for _ in range(K) :
    a = int(input())
    line_list.append(a)
    line_sum += a

stan_len = line_sum // N
final = 0
while True :
    final = 0
    for i in line_list :
        final += i // stan_len

    if final < N :
        stan_len = stan_len - 1
    else :
        print(stan_len)
        break

# Case Study
import sys
K, N = map(int, input().split())
leng = [int(sys.stdin.readline()) for _ in range(K)]
start, end = 1, max(leng)

while start <= end :
    mid = (start + end) // 2
    lines = 0
    for i in leng:
        lines += i // mid
        
    if lines >= N :
        start = mid + 1
    else :
        end = mid - 1
print(end)

"""
insight 정리
1. 랜선 총합을 N으로 나눈 정수 값을 자르는 길이의 기준 값으로 설정 후 이를 각 랜선에 적용하여 나오는 결과를 보며 기준값 조정 
-> 랜선의 길이를 start, end의 기준으로 두어 이분 탐색을 진행
2. 풀이의 맥락은 비슷했는데, 이분 탐색에 대한 정확한 정의를 이해하고 있지 못했음
3. start, end 값의 설정 과정과 최대 랜선의 길이를 구하기 위해 while 조건을 어떻게 설정했는지 체크하기
"""

# ----------------------------------------------------------------------------
