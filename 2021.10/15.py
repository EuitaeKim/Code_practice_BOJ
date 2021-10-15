# 1. 19944 - 문제이름 (https://www.acmicpc.net/problem/19944)
"""
문제 설명
INPC 운영진들은 고심 끝에 뉴비를 1학년 혹은 2학년인 학생으로 정의 내렸고
뉴비를 정의하는 김에 올드비와 TLE도 정의 내리기로 하였습니다.
올드비는 N학년 이하이면서 뉴비가 아닌 학생으로 정의하기로 하였고 TLE은 뉴비도 아니고
올드비도 아닌 학생으로 정의하였습니다.
N과 M이 주어졌을 때, M학년이 뉴비인지 올드비인지 TLE인지 구별해 주세요.
"""

# 내 풀이
n, m = map(int, input().split())
new = [1, 2]
if m in new :
    print('NEWBIE!')
else :
    if m <= n :
        print('OLDBIE!')
    else :
        print('TLE!')

# Case Study
a,b=map(int,input().split())
print("NEWBIE!" if b<3 else "TLE!" if a<b else "OLDBIE!")

"""
insight 정리
1. 이렇게도 풀 수 있구나를 참고하기
"""

# ----------------------------------------------------------------------------

# 2. 16199 - 나이 계산하기 (https://www.acmicpc.net/problem/16199)
"""
문제 설명
한국에서 나이는 총 3가지 종류가 있다.

만 나이: 국제적인 표준 방법이다. 한국에서도 법에서는 만 나이만을 사용한다.
세는 나이: 한국에서 보통 나이를 물어보면 세는 나이를 의미한다.
연 나이: 법률에서 일괄적으로 사람을 구분하기 위해서 사용하는 나이이다.

어떤 사람의 생년월일과 기준 날짜가 주어졌을 때,
기준 날짜를 기준으로 그 사람의 만 나이, 세는 나이, 연 나이를 모두 구하는 프로그램을 작성하시오.
"""

# 내 풀이
import datetime as dt

y1, m1, d1 = map(int, input().split())
y2, m2, d2 = map(int, input().split())

dt1 = dt.datetime(y1, m1, d1)
dt2 = dt.datetime(y2, m2, d2)
td = dt2 - dt1
print(f"{td.days // 365}\n{y2-y1+1}\n{y2-y1}")

# Case Study
y1, m1, d1 = map(int, input().split())
y2, m2, d2 = map(int, input().split())
man_old = 0
if m1 < m2: 
    man_old = y2-y1
elif m1 == m2: 
    if d1 <= d2:
        man_old = y2-y1
    else:
        man_old = y2-y1-1
else:
    man_old = y2-y1-1
count_old = y2-y1+1
year_old = y2-y1
print(man_old)
print(count_old)
print(year_old)

"""
insight 정리
1. 하나하나 뜯어보면 이해가 될 줄 알았는데, 왜 그런지 자꾸봐도 이해가 안됨.. 계속 복습해야 할 듯
"""

# ----------------------------------------------------------------------------
