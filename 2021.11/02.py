# # 1. 1620 - 나는야 포켓몬 마스터 이다솜 (https://www.acmicpc.net/problem/1620)
# """
# 문제 설명
# 오박사 : 그럼 다솜아 이제 진정한 포켓몬 마스터가 되기 위해 도감을 완성시키도록 하여라.
# 일단 네가 현재 가지고 있는 포켓몬 도감에서 포켓몬의 이름을 보면 포켓몬의 번호를 말하거나,
# 포켓몬의 번호를 보면 포켓몬의 이름을 말하는 연습을 하도록 하여라. 나의 시험을 통과하면,
# 내가 새로 만든 도감을 주도록 하겠네.
# """

# # 내 풀이
# import sys
# n, m = map(int, sys.stdin.readline().split())
# dic = {i:sys.stdin.readline().rstrip() for i in range(1, n+1)}

# for i in range(m) :
#     a = sys.stdin.readline().rstrip()
#     try :
#         a = int(a)
#         print(dic[a])
#     except :
#         print(dic)

# # Case Study
# import sys
# input = sys.stdin.readline
# n, m = map(int, input().split())
# dic_n = {}
# dic_s = {}
# for i in range(n) :
#     value = input().strip()
#     dic_n[str(i+1)] = value
#     dic_s[value] = i + 1

# for j in range(m) :
#     quest = input().strip()
#     if quest.isdigit() :
#         print(dic_n[quest])
#     if quest.isalpha() :
#         print(dic_s[quest])

# """
# insight 정리
# 1. 리스트를 하나만 쓰면 시간초과가 뜨는데, 같은 길이의 딕셔너리를 2개를 쓰면 시간초과가 나지 않는다..라
# 2. 딕셔너리가 이정도로 시간 효율적인 자료 구조인지 처음 알게되서(어이없어서) 30분동안 멍때림..
# """