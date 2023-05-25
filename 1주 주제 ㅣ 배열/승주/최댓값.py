# 리스트 입력받아서 최댓값 찾기

# 9번 반복
nums=[]
# 첫째 줄부터 아홉 번째 줄까지 한 줄에 하나의 자연수가 주어짐
for i in range(9): # 9번 반복 진행
    nums.append(int(input())) # nums리스트에 값을 입력 받아서 넣어주기
max_num = max(nums) # max_num 변수에 max 함수를 이용해서 최댓값 담아주기
max_index = nums.index(max_num)+1 # 숫자는 0부터 시작되기 때문에 +1를 해줌.
print(max_num) # 첫째 줄에 최댓값 출력
print(max_index) # 둘째 줄에 최댓값이 몇 번째 수인지 출력