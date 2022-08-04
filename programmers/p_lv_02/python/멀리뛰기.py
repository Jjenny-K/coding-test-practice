# 피보나치 수 # 동적계획법 # 조합

# 멀리뛰기에 사용될 칸의 수 n이 주어질 때, 끝에 도달하는 방법의 수에 1234567을 나눈 나머지 출력


def solution_001(n):
    # 끝에 도달하는 방법의 수를 피보나치 수열로 보고 풀이
    a, b = 0, 1

    for i in range(n):
        a, b = b, a + b

    return b % 1234567


def solution_002(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    return solution_002(n - 1) + solution_002(n - 2)


# run result
n_001 = 4  # answer = 5
print(solution_001(n_001))
print(solution_002(n_001))