# 여러줄 입력받는 상황, 런타임에러 발생 
import sys
# 도시 개수 입력받기
n = int(sys.stdin.readline())

# 출발도시부터 각 도시까지 도로 길이 받기(n-1개)
km_list = list(map(int, sys.stdin.readline().split()))

# 각 도시의 주유소의 리터당 가격
l_list = list(map(int, sys.stdin.readline().split()))

# 기름을 최소한의로 넣으면 = 최소비용
# 각 도시를 A , B로 두고 비교하면
# 각 주유소 l_list[0] ~ [n-1] 까지(마지막 주유소 제외)
# 출발지를 A, 도착지B 예를 들면
# A가 더 저렴할 시 주유금액 = A금액으로 지정 * 거리
# 그리고 다음 주유지금액과 비교해서 더 저렴한 금액일 경우
# 주유 금액을 n금액으로 지정 후 다시 * 거리

# cl  = 현재 가장 저렴한 주유 금액
cl = l_list[0]

# cnt = 최종 금액
# 처음에는 어쩔 수 없이 index[1] 까지 이동하기 위해 충전해야함
cnt = []
a = cl * km_list[0]
cnt.append(a)

# 가장 저렴한 주유지 index까지 각 주유지를 비교하기
# 마지막 주유지는 제외하기 위해 n-1까지만 확인
for i in range(1, n-1):
    if cl > l_list[i]:
        cl = l_list[i]
        b = cl * km_list[i]
        cnt.append(b)
    else: 
        b = cl * km_list[i]
        cnt.append(b)

print(sum(cnt))
