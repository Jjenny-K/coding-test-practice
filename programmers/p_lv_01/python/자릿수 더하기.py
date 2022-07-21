# 10진법 # 연산

# 자연수 n의 각 자릿수의 합 출력


def solution_001(n):
    return sum(map(int, str(n)))


def solution_002(n):
    return n if n < 10 else (n % 10) + solution_002(n // 10)


# run result
n_001 = 987  # answer = 24
print(solution_001(n_001))
print(solution_002(n_001))