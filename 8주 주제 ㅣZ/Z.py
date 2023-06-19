
'''
또 다른 규칙을 찾으면 첫번째 칸의 우측으로 +1 +3 +1 + 11이 반복되면서 증가된다.
                      첫번째 칸의 아래로는 +2 +6 +2 +22 가 반복되면서 증가하게 된다.
그 좌표의 7,3의 경우 7/4은 몫이 1이고 나머지가 3이 되니까 0 + 16(한세트)+1+3 = 20위치에서 밑으로 3번째니까 + 2 + 6 = 28이 된다. 
그 후 나머지 값만큼 나아가면 그 값이 나오게 된다.
'''
n,r,c = map(int, input().split())
result = 0

row_list = [1, 3, 1, 11] # 오른쪽으로
heat_list = [2, 6, 2, 22] # 아래로

heat_share = c//4
heat_rest = c%4
result = heat_share * 32
for i in heat_list[:heat_rest]:
    result+=i
print(result) # 42

print(result ** 2)







'''
# 결론은 원하는 좌표의 나머지 값을 이용해서 계속 증가 시켜준다.
# n = 숫자
# r = 가로(행)
# c = 세로 (열)
n , r, c = map(int, input().split())
result = 0
# 가로 증가폭 리스트 
row_list = [1, 3, 1, 11] # 2행= +1, 3행 = 1+3, 4행 = 1+3+1 이 된다.
# 세로(열) 증가폭 리스트
heat_list = [2, 6, 2, 22]

# c열 구하기
heat_share = c//4
heat_rest = c%4
print(heat_share)
print(heat_rest)


if heat_rest != 0:
    result += heat_share * sum(heat_list)
    for i in heat_list[:heat_rest]:
        result += i
        
print(result)


# r 행 c열
# r // 4 의 값을 row_list sum값을 곱해줌
row_share = r//4
row_rest = r % 4
print(row_share)
print(row_rest)

if row_rest != 0:
    result = row_share * sum(row_list)
    for i in row_list[:row_rest]:
        result += i
print(result)
'''






# (r,c)의 위치는 result 값이지만 0부터 시작하기때문에 몇번째 도달하는지는 +1를 해줘야함
# 만약 나머지가 발생할 경우 [: 나머지] 만큼 더 더해줌

# 일단 원해는 행 위치에 도착시킴


# 나머지 값을 이용해서 시작값에서 rest번까지 list 다 더하기
#print(row_share)
#print(row_rest)

# 지금 현재 cnt위치에서 바로 아래덩어리 맨 앞값 까지는 +32임
# 결론은 r//4 * 32 값을 cnt에 더해준다


# 여기서 heat_rest-1만큼 다시 더해줌
'''
# 가로부터 한번 달려보자
# 숫자는 0부터 출발
cnt = 0
if r >= 4:
    if r%4 == 0:
        cnt = (r//4) * (1+3+1)
    elif r%4 == 1:
        cnt = (r//4) * (1+3+1)+11
    elif r%4 == 2:
        cnt = (r//4) * (1+3+1)+11 + 1
    elif r%4 == 3:
        cnt = (r//4) * (1+3+1)+11+1+3
elif r < 4:
    if r%4 == 1:
        cnt = 0
    elif r%4 == 2:
        cnt = 1
    elif r%4 == 3:
        cnt = 4
print(cnt)
if c >= 4:
    if c%4 == 0:
        cnt += (c//4) * (2 +6 +2+22)
    elif c%4 == 1:
        cnt += (c//4) * (2 +6 +2)+22
    elif c%4 == 2:
        cnt += (c//4) * (2 +6 +2)+22+2
    elif c%4 == 3:
        cnt += (c//4) * (2 +6 +2)+22+2+6
elif c < 4:
    if c%4 == 1:
        cnt += 0
    elif c%4 == 2:
        cnt += 2
    elif c%4 == 3:
        cnt += 6
   
print(cnt+3) 
'''
    


'''
16개씩 나눠주기
len이 n-1개인 리스트를 n-1개 생성한다고 생각하기

그러면 가로는 16 * n-1개 숫자가 가로로 이어짐 0 1 4 5 16 17 20 21
                                           2 3 6 7 18 19 22 23
                                           8 9 12 13 24 25 28 29

그러면 위치는 
몇번쨰 덩어리 인지 가로 부터 확인하기
n / 4 하면 몇번째 덩어리 위치인지 확인하기

다음으로 세로 확인하기
n / 4 하면 세로 몇번째 덩어리 위치인지 확인하기

n/4 가 구해지면 그 덩어리 안에는 16개의 숫자가 존재 그럼

그 덩어리를 다시 확인하기

n, chunk_len = map(int, input().split()) 
lst = []
list_chunked = []
 

# 16개의 숫자가 존재하는 한 덩어리 만들어 주기
# 원하는 길이로 리스트를 나눠서 하나의 리스트로 묶어서 반환
def list_chunk(lst, chunk_len):
    return [lst[i:i+chunk_len] for i in range(0, len(lst), chunk_len)]

lst = list(range(0,n)) # 0~n-1까지의 리스트 생성 if 30 >> 0~29까지 총 30개
#print("분할 전 : ", lst)

# 나누고 싶은 리스트와 몇개씩 분할 할것인지 입력
list_chunked = list_chunk(lst, 16) 
#print("분할 후 : ", list_chunked)


 좌표의 가로 덩어리 위치 찾고
 좌표의 세로 덩어리 위치를 찾아서
 큰 덩어리 n/4에서 나머지 값 위치가
 덩어리 안에서의 그 좌표의 위치가 된다
 큰 덩어리 좌표 위치 * 덩어리 첫 시작과 마지막끝을 기억해라
 그리고 그 숫자의 리스트를 출력해서 그림을 그리게 된다면
ex) 7.11라고 하면 7 / 3 을하면 몫이 1이고 나머지가 3이 되게 된다.
그럼 두번째 덩어리에서 3번째 줄이다.
두번째 덩어리

'''













# n 입력 받기

# (2*n) * (2*n) 만큼의 숫자를 list에 담아주기

# list값을 4개로 쪼개주기
'''
[[0,1,2,3], [4,5,6,7], 
 [8,9,10,11], [12,13,14,15] ]
'''


# 마지막으로 실제로 생성된 그림은
# 가로 n-1 , 세로 n-1
# 그 앞에 묶은 리스트를 n-1 묶어준다

'''
16개씩 나눠주기
len이 n-1개인 리스트를 n-1개 생성한다고 생각하기

그러면 가로는 16 * n-1개 숫자가 가로로 이어짐 0 1 4 5 16 17 20 21
                                           2 3 6 7 18 19 22 23
                                           8 9 12 13 24 25 28 29

그러면 위치는 
몇번쨰 덩어리 인지 가로 부터 확인하기
n / 4 하면 몇번째 덩어리 위치인지 확인하기

다음으로 세로 확인하기
n / 4 하면 세로 몇번쨰 덩어리 위치인지 확인하기

n/4 가 구해지면 그 덩어리 안에는 16개의 숫자가 존재 그럼

그 덩어리를 다시 확인하기

'''