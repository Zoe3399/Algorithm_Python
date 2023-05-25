'''
에라토스테네스의 체 <<  일정한 수에서 체에 거르는 방식 ,소수를 구하는 알고리즘

1 != 소수 << 삭제
2 == 소수 << 2의 배수 전부 삭제
3 == 소수 << 3의 배수 전부 삭제
... 이런식으로 수를 걸러내고 남은 수가 소수

 1. 2부터 시작해서, 특정한 숫자보다 1작은 수까지 확인하면서
 2. 한번이라도 약수가 존재하면 x%i == 0: << 소수가 아님
 3. 삭제
 4. x%i != 0: True

# m ~ n 이하의 소수 출력하기
m, n = map(int,(input().split()))
num = []
prime = [] # 소수

# 1은 소수이기 때문에 2부터
for i in range(2, n+1):
    for j in range(2, i+1):
        if i % j == 0:
            num.append(i)
    if num.count(i) <=3:
        prime.append(i)

[print(i) for i in prime]

# >> 이렇게하게되면 문제점 : 시간초과 발생
# 그래서 사용하는게 에라토스테네스의 체

1. 2부터 소수를 구하고자 하는 모든 수 나열
2. 2 = 소수 , 자기 자신 제외한 2의 배수 모두 삭제
3. 3 = 소수 , 자기 자신 제외한 3의 배수 모두 삭제
4. 5, 7도 동일하게 진행하면 구하는 구간으이 모든 소수가 남음

 n까지의 에라토스테네스
def prime_list(n):
    
    # 에라토스테네스의 체 기초화
    sieve = [True] * n  # n개 요소에 True 설정(소수로 간주), sieve는 전부 True 인 상태
    # n의 최대 약수가 sqrt(n) 이하이므로 i = sqrt(n)까지 검사
    # sqrt = 제곱근 함수, n의 제곱근을 반환(n에 루트를 씌운 값을 반환)
    # 반환형은 float타입, 만약, 음수가 들어오면 error 발생
    # math.sqrt(4) >> 4의 제곱근인 2를 반환

    
    m = int(n ** 0.5)
    for i in range(2,m+1): # 1은 소수이기 때문에 2부터 시작해서
        if sieve[i] == True: # i가 소수인 경우
            for j in range(i+i,n,i): # i이후, i의 배수들만
                sieve[j] = False # 전부 False 판정

    # 소수 목록 산출
    [i for i in range(2,n) if sieve[i] == True]
'''
'''
# 하지만 우리가 구해야하는건 n~m까지이다
m, n = map(int,(input().split()))
n += 1 # 미리 n+1 해줌(for문을 위해서)
prime_list = [True]* n # n개의 [True]가 있는 리스트 생성

for i in range(2, int (n**0.5)+1):  # n의 제곱근까지만 검사
    if prime_list[i]:  # prime[i]가 True일때
        for j in range(i*2, n, i): # prime 내 i의 배수들을 
            prime_list[j] = False # False로 변환

for i in range(m, n):
    if prime_list[i]:
        print(i)
'''
        
# math.sqrt함수 사용
import math
m, n = map(int,(input().split()))

#n += 1 # 미리 n+1 해줌(for문을 위해서)
prime_list = [True]* (n+1) # n개의 [True]가 있는 리스트 생성
prime_list[1] = False

for i in range(2 ,int(math.sqrt(n))+1):  # n의 제곱근(루트) 함수 사용
    if prime_list[i] == True:  # prime[i]가 True일때
        for j in range(i*2, n+1, i): # prime 내 i의 배수들을 
            prime_list[j] = False # False로 변환

for i in range(m, n+1):
    if prime_list[i]:
        print(i)
    

# 비교하기        
# for i in range(2, int (n**0.5)+1):
# for i in range(2,int(math.sqrt(n))+1):
