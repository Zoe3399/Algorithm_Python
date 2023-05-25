# https://www.acmicpc.net/problem/2480

# 공백으로 수 입력 받아 list 생성 
nums = list(map(int, input().split()))
s_nums = set(nums)
overlap = sum(nums) - sum(s_nums)
max_num = max(s_nums)

if len(set(nums)) == 1: print(10000+nums[0]*1000) 
elif len(set(nums)) == 2: print(1000+overlap*100)
elif len(set(nums)) == 3: print(max_num*100)