# 정수 n의 약수를 모두 더한 값 출력


def solution_001(n):
    answer = 0
    for i in range(n, 0, -1):
        if n % i == 0:
            answer += i
    print(answer)


def solution_002(n):
    # print(sum(i for i in range(n, 0, -1) if n % i == 0))
    print(sum(list(filter(lambda i: not n % i, range(n, 0, -1)))))


def solution_003(n):
    print(n + sum([i for i in range(1, (n // 2) + 1) if n % i == 0]))


# run result
n_001 = 12
solution_001(n_001)
solution_002(n_001)
solution_003(n_001)