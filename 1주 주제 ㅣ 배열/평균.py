# 과목수 n 입력받기
n = int(input())

# 성적 공백으로 list 입력받기
s_list = list(map(int, input().split()))

# 제일 높은 성적
m = max(s_list) 

# 점수 합
s_score = 0

# 새로운 성적 구해서 다 더하기
for i in s_list:
    s_score = i/m*100 + s_score

# 새로 구한 점수 평균구하기
print(s_score/n) 