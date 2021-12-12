# 1. 10825 - 국영수 (https://www.acmicpc.net/problem/10825)
"""
문제 설명
도현이네 반 학생 N명의 이름과 국어, 영어, 수학 점수가 주어진다. 이때, 다음과 같은 조건으로 학생의 성적을 정렬하는 프로그램을 작성하시오.

1. 국어 점수가 감소하는 순서로
2. 국어 점수가 같으면 영어 점수가 증가하는 순서로
3. 국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로
4. 모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로 (단, 아스키 코드에서 대문자는 소문자보다 작으므로 사전순으로 앞에 온다.)
"""

# 내 풀이
import sys
input = sys.stdin.readline
n = int(input())

li = []
for _ in range(n) :
    a, b, c, d = map(str, input().rstrip().split())
    li.append((a, int(b), int(c), int(d)))

final = sorted(li, key = lambda x : (-x[1], x[2], -x[3], x[0]))
for i in final :
    print(i[0])

"""
insight 정리
1. sort는 입력 리스트 자체의 순서를 바꾸는 것, sorted는 원본은 그대로 두고 새로운 리스트를 생성해 순서를 바꾸는 것
2. 리스트에 튜플 형식의 데이터를 넣는 경우와 딕셔너리에 key, value를 활용하는 경우 sorted를 활용해 정렬 방식을 디테일하게 잡을 수 있음 (lambda goooooooood)
3. 다만 문제 설명처럼 문자 정렬의 경우 아스키 코드 베이스로 정렬을 진행하기 때문에 문자열의 경우 주의할 것
"""