# https://solved.ac/profile/playdev7
# 1541 / 잃어버린 괄호
# 문제
# 자연수들의 덧셈과 뺄셈들로 이루어진 수식이 주어진다.
# 위 수식에 적절히 괄호를 쳐서 최소의 값을 출력시켜라.

# ex) 55 - 50 + 40 => 55 - (50+40) = -35

# 입력 - 공백없이 수식이 한줄로 쭉 주어진다
# 출력 - 가능한 최소의 값을 출력시킨다.

# 풀이 - 뺄셈이 클 수록 유리하다.

problem = input()

plus = "+"
minus = "-"

answer = 0

# 연산 기호를 공백을 포함하도록 변환
problem = problem.replace(plus, " + ")
problem = problem.replace(minus, " - ")

# 이후 공백을 기준으로 리스트화
problem = list(problem.split(" "))

answer = 0
current = 1

# minus 가 오는 순간 괄호를 치면 된다.
for i in problem:
    if i is minus:
        current = -1
        pass
    elif i is plus:
        pass
    else:
        answer += int(i) * current

print(answer)