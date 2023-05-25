'''
Euclidean Algorithm
 1. x(큰변)에 y(작은변)를 나눠서 나머지를 구하기
    # x % y = r
 2. y(작은변)를 나머지로 나눈 나머지를 구하기
     y % r = r`
 3. 나머지가 0이 될때까지 2번을 반복하기
 4. 나머지가 0일때, 작은 변이 최대 공약수
'''

''' C언어로 구현
int gcd(int x, int y){
    if (y == 0){ // 나머지가 0이 될 때
        return x; // 최대 공약수 출력
    }
    return gcd(y, x%y);
    # 재귀호출
    # x값에 y 넣어주고, y에 r을 넣어주는 방법으로 반복
}
'''
'''
유클리드 최대공약수
a,b = map(int, input().split())
def gcd(a,b):
    if b == 0:
        print(a)
    else:
        gcd(b, a%b)
gcd(a,b)
'''

# 최대공약수 먼저 구하기
a,b = map(int, input().split())

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)

# 최소 공배수 = a, b의 곱을 최대 공약수로 나누면 나오게된다
def lcm(a, b):
    lcm_num = a*b / gcd(a,b)
    print(int(lcm_num))

lcm(a, b)