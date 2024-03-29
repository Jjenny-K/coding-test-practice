# 수학 # 약수 # 연산 # sum

# 정수 n의 약수를 모두 더한 값 출력


def solution_001(n):
    answer = 0

    for i in range(n, 0, -1):
        if n % i == 0:
            answer += i

    return answer


def solution_002(n):
    # return sum(i for i in range(n, 0, -1) if n % i == 0)
    return sum(list(filter(lambda i: not n % i, range(n, 0, -1))))


def solution_003(n):
    return n + sum([i for i in range(1, (n // 2) + 1) if n % i == 0])


# run result
n_001 = 12  # answer = 28
print(solution_001(n_001))
print(solution_002(n_001))
print(solution_003(n_001))