# https://solved.ac/profile/playdev7
# 11399 / ATM

# 문제
# 손님 수와 손님당 대기시간이 주어진다. 손님의 순서를 바꿔서 대기시간을 최소화 했을 때 시간의 총 합을 구하는 문제.

# 입력
# 사람 수 N이 주어진다.
# 다음 줄에 N개의 시간이 주어진다.

# 출력
# 대기시간을 최소화 한 다음 N명의 대기시간 총합을 출력해라.

N = int(input())
Persons = list(map(int, input().split()))

Persons.sort()

answer = 0
for i in range(N):
    answer += Persons[i]
    for j in range(i):
        answer += Persons[j]

print(answer)