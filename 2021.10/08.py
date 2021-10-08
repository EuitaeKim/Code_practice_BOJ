
# 1. 10699 - 오늘 날짜 (https://www.acmicpc.net/problem/10699)
"""
문제 설명
서울의 오늘 날짜를 출력하는 프로그램을 작성하시오.
채점 서버 시간대(Timezone)는 UTC + 0 이다.
다음은 채점 서버에서 KST 시간으로 2018년 3월 21일 오후 2시 7분 38초에
date 명령어를 실행시킨 결과이다.
Wed Mar 21 05:07:38 UTC 2018
"""

# 내 풀이
import datetime
print(str(datetime.datetime.now())[:10])

"""
insight 정리
1. 평소에 시간을 출력하는 일이 별로 없어 나중에 까먹을 것 같아 기록
"""

# ----------------------------------------------------------------------------

# 2. 14645 - 와이버스 부릉부릉 (https://www.acmicpc.net/problem/14645)
"""
문제 설명
첫 줄에 출발역과 종착역을 제외한 정거장의 수 N(1 ≤ N ≤ 100,000)과 출발역에서
탑승하는 사람의 수 K(1 ≤ K ≤ 10,000)가 주어진다. 둘째 줄부터 N개의 줄에 걸쳐 
각 줄마다 i번째 정거장에서 탑승하는 인원 A와 하차하는 인원 B가 주어진다.
(0 ≤ A, B ≤ 10,000) 종착역에 도착했을 때, 버스 운전수의 이름을 출력해라.
"""

# 내 풀이
print('비와이')

"""
insight 정리
1. 입력값을 활용하지 않는 경우 굳이 input으로 받을 필요는 없다.
"""

# ----------------------------------------------------------------------------

# 3. 18301 - Rats (https://www.acmicpc.net/problem/18301)
"""
문제 설명
Douglas decides to count the number of rats living in his area.
It is impossible for him to find all rats, as they tend to be well hidden.
However, on the first day of the new year, Douglas manages to capture n1 rats,
and marks each of them with an ear tag before releasing them.
On the second day of the new year, Douglas captures n2 rats,
and observes that n12 of them had been marked during the first day.

Douglas is asking for your help to estimate the total number of rats in his area.
Looking up in your statistics textbook, you propose using the Chapman estimator N, given by:
N := ⌊(n1 + 1)(n2 + 1)/(n12 + 1) - 1⌋
where ⌊x⌋ is the floor of a real number x, i.e., the closest integer less than or equal to x.
"""

# 내 풀이
import math

A, B, C = map(int, input().split())
print(math.floor((((A + 1) * (B + 1)) / (C + 1)) - 1))

"""
insight 정리
1. 올림은 ceil, 내림은 floor 기억해두기
"""

# ----------------------------------------------------------------------------






