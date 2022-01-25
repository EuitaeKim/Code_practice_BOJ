# 1. 24337 - 가희와 탑 (https://www.acmicpc.net/problem/24337)
"""
문제 설명
가희와 단비 사이에 있는 건물의 개수 N과 가희가 볼 수 있는 건물의 개수 a, 단비가 볼 수 있는 건물의 개수 b가 주어집니다.
사전 순으로 가장 앞서는 N개의 건물 높이 정보를 출력해 주세요.
"""

# 내 풀이
import sys
input=sys.stdin.readline
n,a,b=map(int, input().split())
check_a=False

if a >= b:
    final=[i for i in range(1, a+1)]
    if b-1 != 0:
        final_2=[j for j in range(b-1, 0, -1)]
        final+=final_2
else:
    final=[i for i in range(b, 0, -1)]
    if a-1 != 0:
        final_2=[j for j in range(1, a)]
        final=final_2+final
    else:
        check_a=True

if len(final)>n:
    print(-1)
elif len(final)==n:
    print(' '.join(map(str, final)))
elif len(final)<n:
    diff=n-len(final)
    if check_a:
        final=final[:1]+([1]*diff)+final[1:]
        print(' '.join(map(str, final)))
    else:
        final=([1]*diff)+final
        print(' '.join(map(str, final)))

"""
insight 정리
1. 문제 자체의 난이도는 어렵지 않았지만, 반례 직접 찾기 + 구성적 문제 유형에 쎄게 당한 문제..
2. 사전 순으로 가장 앞선 것을 출력해야 한다는 조건을, 발생할 수 있는 경우의 수에 모두 대입시키지 못해 많이 틀렸다.
3. 반례 리스트를 알 수 있었다면 시간이 오래 걸리지 않았을 듯. 반례를 구할 수 없는 상황에서 반례를 직접 만들어 낼 수 있는
힘을 길러야겠다.
"""

# ----------------------------------------------------------------------------

# 2. 1013 - Contact (https://www.acmicpc.net/problem/1013)
"""
문제 설명
최근 김동혁 박사는 아레시보 전파망원경에서 star Vega(직녀성) 으로부터 수신한 전파 기록의 일부를 조사하여
그 전파들의 패턴을 분석하여 아래와 같이 기록하였다. (100+1+ | 01)+
김동혁 박사는 다양한 전파 기록 중에서 위의 패턴을 지니는 전파를 가려내는 프로그램을 필요로 한다.
이를 수행할 수 있는 프로그램을 작성하라.
"""

# 내 풀이
import re
import sys
input=sys.stdin.readline

check=re.compile('(100+1+|01)+')
for _ in range(int(input())):
    num=str(input().rstrip())
    m=check.fullmatch(num)
    if m:
        print('YES')
    else:
        print('NO')

"""
insight 정리
1. 처음으로 풀어본 정규 표현식 문제. 생각보다 어렵지 않았고, 어느 정도 숙련되면 쉽게 해결할 수 있는 유형이라고 판단됨.
"""