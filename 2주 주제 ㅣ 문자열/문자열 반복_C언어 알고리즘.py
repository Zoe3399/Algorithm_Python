t= int(input())
p = []

for i in range(t):
    
    r, s = map(str, input().split())
    r = int(r) # 숫자 정수로 변경
    result_list = []
    for i in range(len(s)):
        for j in range(r):
            result = s[i] * r
        result_list.append(result)
    p.append(''.join(result_list))
    #print() # 출력 후 다음 값 받기 위해서 줄바꿈해주기
    
for i in p:
    print(i)

'''
t= int(input())

for i in range(t):
    
    r, s = map(str, input().split())
    r = int(r) # 숫자 정수로 변경
    
    for i in range(len(s)):
        for j in range(r):
            print(s[i], end='')
    print() # 출력 후 다음 값 받기 위해서 줄바꿈해주기
print()
'''


'''
int main() {
    int T, R;
    char S[21];
    
    scanf("%d", &T);
    
    while (T--) {
        scanf("%d %s", &R, S);
        
        // i가 0이고, i가 문자열 S길이만큼 반복하고, i는 증가
        for (int i = 0; i < strlen(S); i++) {
            // j가 0이고, R보다 작을 때 r 증가
            for (int j = 0; j < R; j++)
                printf("%c", S[i]);
        }
 
        printf("\n");
    }
    return 0;
}
'''