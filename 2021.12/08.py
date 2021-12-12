# 1. 11728 - 배열 합치기 (https://www.acmicpc.net/problem/11728)
"""
문제 설명
정렬되어있는 두 배열 A와 B가 주어진다. 두 배열을 합친 다음 정렬해서 출력하는 프로그램을 작성하시오.
"""

# 내 풀이
import sys
input = sys.stdin.readline

a, b = map(int, input().split())
li = list(map(int, input().split()))
li_2 = list(map(int, input().split()))

final = ''
i = j = 0

while True :
    if li[i] <= li_2[j] :
        final += str(li[i]) + ' '
        i += 1

    else :
        final += str(li_2[j]) + ' '
        j += 1
    
    if i == a or j == b :
        break

if i == a :
    while j != b :
        final += str(li_2[j]) + ' '
        j += 1
elif j == b :
    while i != a :
        final += str(li[i]) + ' '
        i += 1

print(final[:-1])

# Case Study
import sys
input = sys.stdin.readline
 
n, m = map(int, input().split())
nmlist = list(map(int, input().split())) + list(map(int, input().split()))

print(' '.join(map(str, sorted(nmlist))))

"""
insight 정리
1. 단순히 두 리스트를 합친 후 sort를 쓰면 시간 초과가 날 줄 알았는데.. 그게 맞았던 문제.
2. 만약 두 리스트가 정렬되어 있지 않았다면, 시간 초과가 나지 않았을까?
이유 : 파이썬의 sort(), sorted() 계열 함수는 삽입 정렬과 병합 연산을 기반으로 하는 팀정렬 알고리즘을 사용
내 풀이의 병합 정렬과, Case Study의 팀 정렬은 모두 O(nlogn)의 시간 복잡도를 가짐
그러나 팀 정렬은 평균적인 성능을 고려한다면 병합 정렬보다 성능이 좋은 경우가 있다고 함. 그리고 이 문제가 예시가 된다고 생각함
주어진 두 리스트는 이미 정렬이 되어 있기 때문에, 삽입 정렬, 병합 수행에서 시간이 많이 절약된다고 생각하기 때문
"""
