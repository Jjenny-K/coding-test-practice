# 수학 # 피보나치 수 # 동적계획법

# 피보나치 수: F(0) = 0, F(1) = 1, F(n) = F(n - 1) + F(n - 2)
# 2 이상의 n이 주어졌을 때, n번째 피보나치 수를 1234567로 나눈 나머지 출력

def solution_001(n):
    if n < 3:
        if n == 0:
            return 0
        else:
            return 1

    fib = [0, 1, 1]
    for i in range(3, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])

    return fib[n] % 1234567


def solution_002(n):
    a, b = 0, 1

    for i in range(n):
        a, b = b, a + b

    return a % 1234567


def solution_003(n):
    f_list = [0, 1]

    for i in range(2, n + 1):
        f_list.append((f_list[i - 2] % 1234567 + f_list[i - 1] % 1234567) % 1234567)

    return f_list[-1]


# run result
n_001 = 5  # answer = 5
print(solution_001(n_001))
print(solution_002(n_001))
print(solution_003(n_001))