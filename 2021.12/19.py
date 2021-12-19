# 1. 2630 - 색종이 만들기 (https://www.acmicpc.net/problem/2630)
"""
문제 설명
여러개의 정사각형칸들로 이루어진 정사각형 모양의 종이가 주어져 있고, 각 정사각형들은 하얀색으로 칠해져 있거나 파란색으로 칠해져 있다.
주어진 종이를 일정한 규칙에 따라 잘라서 다양한 크기를 가진 정사각형 모양의 하얀색 또는 파란색 색종이를 만들려고 한다.
입력으로 주어진 종이의 한 변의 길이 N과 각 정사각형칸의 색(하얀색 또는 파란색)이 주어질 때 잘라진 하얀색 색종이와 파란색 색종이의 개수를 구하는 프로그램을 작성하시오.
"""

# 내 풀이
import sys
input = sys.stdin.readline

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
check_list = [paper]

def div(list) :
    li_1 = list[0:len(list)//2][0:len(list)//2]
    li_2 = list[0:len(list)//2][len(list)//2:len(list)]
    li_3 = list[len(list)//2:len(list)][0:len(list)//2]
    li_4 = list[len(list)//2:len(list)][len(list)//2:len(list)]
    return [li_1, li_2, li_3, li_4]

blue = 0
white = 0
while len(check_list) != 0 :
    li = check_list[0]
    blue_count = 0
    for i in range(0, len(li)) :
        for j in range(0, len(li)) :
            if li[i][j] == 1 :
                blue_count += 1

    check = False
    if blue_count == len(li) ** 2 :
        blue += 1
        check = True

    if blue_count == 0 :
        white += 1
        check = True

    if check == False :
        li_2 = div(li)
        check_list = check_list + li_2 

    check_list = check_list[1:]
    check = False

print(blue)
print(white)

# Case Study
import sys
n = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)] 

result = []

def solution(x, y, n) :
  color = paper[x][y]
  for i in range(x, x + n) :
    for j in range(y, y + n) :
      if color != paper[i][j] :
        solution(x, y, n//2)
        solution(x, y + n//2, n//2)
        solution(x + n//2, y, n//2)
        solution(x + n//2, y + n//2, n//2)
        return
  if color == 0 :
    result.append(0)
  else :
    result.append(1)

solution(0, 0, n)
print(result.count(0))
print(result.count(1))

"""
insight 정리
1. 특정 순서에서 내 코드의 30~33줄이 실행되지 않으면서 답이 도출되지 않음. 코드 실행 순서 검토 및 인터넷 검색을 해도 그 원인을 모르겠음..
2. 분할 정복에 대한 내용을 찾아보니, 동적 계획법과 비교하여 설명하는 글들이 많았음. 분할 정복 및 동적 계획법 모두 주어진 Task를 작게 쪼개 하나씩 해결해 나간다는 컨셉은
비슷하나, 분할 정복에서는 세부 Task 별 중복이 없고 동적 계획법은 중복이 있을 수 있다는게 주요 차이점.
3. 2의 이유 때문에 동적 계획법에서는 메모이제이션이, 분할 정복은 재귀 기반의 구간 분할이 중요 포인트임
4. Case Study의 색종이를 같은 길이로 4등분하는 방법(65~68), 특정 구간에서 색을 검토하는 방법(61~64)을 체크해둘 것
5. 저번 백트래킹에서부터 전체 탐색을 위한 재귀 방법이 계속 활용되는 점도 체크해둘 것
"""