# 1. 9019 - DSLR (https://www.acmicpc.net/problem/9019)
"""
문제 설명
네 개의 명령어 D, S, L, R 을 이용하는 간단한 계산기가 있다. 이 계산기에는 레지스터가 하나 있는데,
이 레지스터에는 0 이상 10,000 미만의 십진수를 저장할 수 있다.
여러분이 작성할 프로그램은 주어진 서로 다른 두 정수 A와 B(A ≠ B)에 대하여 A를 B로 바꾸는 최소한의 명령어를 생성하는 프로그램이다.
예를 들어서 A = 1234, B = 3412 라면 다음과 같이 두 개의 명령어를 적용하면 A를 B로 변환할 수 있다.
"""

# 내 풀이
import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    n, m=map(int, input().split())
    que=deque([[n, '']])
    check=[0 for _ in range(10001)]
    check[n]=1
    while True:
        num, ord = que.popleft()

        num_d=(num*2)%10000
        if num_d==m: print(ord+'D', sep='\n'); break
        else:
            if not check[num_d]:
                que.append([num_d, ord+'D'])
                check[num_d]=1

        if num>0 and num-1==m: print(ord+'S', sep='\n'); break
        elif num==0 and 9999==m: print(ord+'S', sep='\n'); break
        else:
            if num==0 and not check[9999]:
                que.append([9999, ord+'S'])
                check[9999]=1
            elif num>0 and not check[num-1]:
                que.append([num-1, ord+'S'])
                check[num-1]=1

        num_st=str(num)
        if len(num_st) != 4:
            num_st = '0'*(4-len(num_st)) + num_st
            
        num_l=int(num_st[1:]+num_st[0])
        if num_l==m: print(ord+'L', sep='\n'); break
        else:
            if not check[num_l]:
                que.append([num_l, ord+'L'])
                check[num_l]=1
        
        num_r=int(num_st[-1]+num_st[:-1])
        if num_r==m: print(ord+'R', sep='\n'); break
        else:
            if not check[num_r]:
                que.append([num_r, ord+'R'])
                check[num_r]=1

"""
insight 정리
1. 13번 틀리고 겨우 맞춘 문제 박제...
2. 주어진 숫자가 4자리가 아닌 경우 숫자 앞에 0을 더해 4자리를 만든 후 L, R 연산을 진행해야 했음
"""



# import sys
# input = sys.stdin.readline
# gear = [[0,0,0,0,0,0,0,0]]+[[int(i) for i in str(input().rstrip())] for _ in range(4)]

# gear_check = [[0,0] for _ in range(5)]

# # 회전할 때 비교되는 인덱스 1) 2 2) 6 2 3) 6 2 4) 6
# for _ in range(int(input())):
#     # a는 회전시킨 톱니바퀴의 번호, b는 정수의 방향
#     a, b = map(int, input().split())
#     if a==0:
#         start=a
#         gear_check[a][0],gear_check[a][1]=1,b
#         while True:
#             b *= -1
#             if gear[start][2]!=gear[start+1][6]:
#                 gear_check[start][0],gear_check[start][1]=1,b
#                 if start+1>4:
#                     break
#                 else:
#                     start+=1
#             else:
#                 break
#     elif a==4:
#         start=a
#         while True:
#             b *= -1
#             if gear[start][2]!=gear[start+1][6]:
#                 gear_check[start][0],gear_check[start][1]=1,b
#                 if start-1<1:
#                     break
#                 else:
#                     start-=1
#             else:
#                 break
#     elif a==2:
#         if gear[a][2]!=gear[a+1][6]:
#             b *= -1
#             gear_check[a+1][0],gear_check[a+1][0]=1,b
#             if gear[a+1][2]!=gear[a+2][6]:
#                 b *= -1
#                 gear_check[a+2][0],gear_check[a+2][0]=1,b
#             else:
#                 pass
#         else:
#             pass 

#         if gear[a-1][2]!=gear[a][6]:
#             b *= -1
#             gear_check[a-1][0],gear_check[a-1][1]=1,b
#         else:
#             pass

#     elif a==3:
#         if gear[a-1][2]!=gear[a][6]:
#             b *= -1
#             gear_check[a-1][0],gear_check[a-1][1]=1,b
#             if gear[a-2][2]!=gear[a-1][6]:
#                 b *= -1
#                 gear_check[a-2][0],gear_check[a-2][1]=1,b
#             else:
#                 pass
#         else:
#             pass 

#         if gear[a][2]!=gear[a+1][6]:
#             b *= -1
#             gear_check[a][0],gear_check[a][1]=1,b
#         else:
#             pass
    
#     idx = -1
#     for j, k in enumerate(gear_check):
#         idx += 1
#         if j:
#             if k==1:
#                 gear[idx] = [gear[idx][7]] + gear[idx][:7]
#             else:
#                 gear[idx] = gear[idx][1:8] + [gear[idx][0]]

# score = 0.5
# total = 0
# for idx, i in enumerate(gear):
#     if idx != 0:
#         score *= 2
#         if i[0]:
#             total += score

# print(score)