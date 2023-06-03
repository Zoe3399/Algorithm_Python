a = input().split('-')
res = sum(map(int,a[0].split('+')))
num = [sum(map(int,i.split('+'))) for i in a[1:]]
for i in num: res-=i
print(res)   



''' 
a = input().split('-')
res = sum(map(int,a[0].split('+')))
for i in a[1:]:
    num = sum(map(int,i.split('+')))
    res -= num
print(res)   



[ 코드 더 간단하게 만들기 ]
# 문자열 입력받기
a = input().split('-')
# a[0] 먼저 res에 대입
res = sum(map(int,a[0].split('+')))
# a[1] 부터 진행
for i in a[1:]:
    # i값에서 '+' 기준으로 나눠서 int형으로 형변환 후 총합
    num = sum(map(int,i.split('+')))
    # 차례대로 뺄셈 진행
    res -= num
print(res)    



[ 처음 작성한 코드 ]
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
