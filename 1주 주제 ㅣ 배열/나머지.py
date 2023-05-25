# 숫자 10개 입력받기
nums = []
for i in range(10): # 10번 반복 진행
    nums.append(int(input())) # nums 리스트에 숫자 입력받기
rest = []

for i in nums:
    # 입력받은 숫자들 %42 한 값들을 전부
    # rest 리스트에 int 값으로 append 하기
    rest.append(int(i % 42)) 

rest_num = set(rest) # 중복제거

print(len(rest_num)) # 서로 다른 나머지 갯수
