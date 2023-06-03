# https://solved.ac/profile/playdev7
# 13305 / 주유소

# 문제
# N개의 도시가 있고 각 도시의 리터당 주유 가격은 value 이다.
# 가장 왼쪽에서 가장 오른쪽으로 이동하고자 할 때 가장 적게 주유되는 비용을 출력하라.

# 입력
# 첫 줄에 도시의 개수 N
# 둘째줄에 도시간 거리 km 이 N-1개
# 셋째줄에 도시의 주유가격 value가 N개

# 출력
# 최소한의 주유 비용을 출력한다.

# 풀이
# 어차피 다음 도시로 넘어가려면 일단 충전해야한다.
# 최저가인 도시까지 일단 충전하며 간다.
# 최저가인 도시에 도착하면 도착지까지 전체를 충전한다.

import sys
input = sys.stdin.readline

N = int(input())
km_list = list(map(int, input().split()))
values = list(map(int, input().split()))

answer = 0

# 마지막 도시의 주유 가격은 의미가 없으므로 뺀다.
values.pop()

min_value = min(values)
min_place = values.index(min_value)

for i in range(min_place):
    if values[i] < values[i+1]:
        values[i+1] = values[i]

for i in range(min_place):
    answer += values[i] * km_list[i]

for i in range(min_place, N-1):
    answer += min_value * km_list[i]

print(answer)
