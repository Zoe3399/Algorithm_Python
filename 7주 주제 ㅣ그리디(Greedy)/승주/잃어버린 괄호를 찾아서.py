# 문자열 입력받기
a = input().split('-')
res = sum(list(map(int,a[0].split('+'))))
for i in a[1:]:
    num = sum(list(map(int,i.split('+'))))
    res -= num
print(res)    


''' 
# 문자열 입력받기
a = input().split('-')
number = []
for i in a:
    b = sum(list(map(int,i.split('+'))))
    number.append(b)

res = number[0]
for i in number[1:]:
    res -= i
print(res)
'''