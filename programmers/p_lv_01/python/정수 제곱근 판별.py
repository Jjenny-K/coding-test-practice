# 양의 정수 n이 임의 양의 정수 x의 제곱일 때 x + 1의 제곱, 아닐 때 -1 출력
import math


def solution_001(n):
    # 제곱의 역연산: ²√x = x^½
    x = n ** 0.5

    # return (x + 1) ** 2 if x % 1 == 0 else -1
    return -1 if x % 1 else (x + 1) ** 2


def solution_002(n):
    return -1 if math.sqrt(n) % 1 else (math.sqrt(n) + 1) ** 2


# run result
n_001 = 121  # answer = 144
print(solution_001(n_001))
print(solution_002(n_001))

n_002 = 3  # answer = -1
print(solution_001(n_002))
print(solution_002(n_002))