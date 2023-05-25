'''
 https://www.acmicpc.net/problem/2675
'''
'''
문자열 S를 입력받기
각 문자를 R번 반복해서
새 문자열 P만들기
출력
'''

# 코드가 너무 길어지는거 같길래 보기 좋게 다시 정리해보기
t = int(input()) # 테스트 케이스 t값 입력 받기
result = [] # 문자 하나씩 곱한 값 담을 리스트 ex) ['aaa', 'bbb', 'ccc']
p = [] # 반복된 문자의 결과값 리스트

for _ in range(t): # t만큼 입력 받기
    # 공백을 기준으로 r, s문자열로 입력 받기
    r, s = map(str, input().split())
    r = int(r) # 반복횟수 r은 정수로 변환
    s_list = list(s) # 문자열 s를 한글자씩 끊어서 담기
    
    for i in s_list: # 리스트 차례대로 출력
        result.append(r * i)
        # 문자를 r만큼 곱한 값을 result 리스트에 담기
        # ex)['aaa', 'bbb', 'ccc'] << 이런식으로 담김
    # 그렇기 때문에 문자열로 바꿔줘서 다시 리스트에 담기
    # ex) 문자열 aaabbbccc 로 바꾼 다음 ['aaabbbccc'] 로 바꿈
    p.append(''.join(result)) 
    # .join() 함수 << 리스트를 문자열로 변환하는 함수
    
    # 리스트 초기화 시켜주기 (매우 중요)
    s_list = []
    result = []

for i in p: # 리스트 p를 차례대로 출력
    print(i)    
    
        
        
    
    



'''
코드가 너무 길어지는거 같길래 보기 좋게 다시 정리해야할듯

t = int(input())
s=[]
new_list = []
p = []

# 반복횟수 = r , 문자열 = s 공백으로 구분
for _ in range(t): # t 만큼 반복해주기
    t_list = list(map(str, input().split())) # 공백으로 문자열 입력 받기
    # 리스트 분리해서 담아주기
    r = (int(t_list[0]))
    s_list.append(t_list[1])
    
    s = [] # s_list 문자열을 한글자씩 끊어서 담을 리스트
    
    # s_list 문자열을 한글자씩 끊어서 담기
    s.append(list(t_list[1])) # 한글자씩 끊어서 s리스트에 append(담기)
    s = sum(s, [])
    
    # 마지막 출력해줄 p_list
    for i in s:
        new_list.append(r * i) # 문자 하나씩 r만큼 곱해주기
    p_list.append(''.join(new_list)) # 곱한값을 문자열 화해서 list에 담기
    
    r_list = []
    s_list = []
    new_list = []
    
for i in p_list:
    print(i)

'''


'''
하나씩 입력받고 출력하기

t= int(input())
s = []

for i in range(t):
    
    r, s = map(str, input().split())
    r = int(r) # 숫자 정수로 변경
    
    for i in range(len(s)):
        for j in range(r):
            print(s[i], end='')
    print() # 출력 후 다음 값 받기 위해서 줄바꿈해주기
print()



'''