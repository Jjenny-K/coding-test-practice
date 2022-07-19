# 두 정수 a, b 사이에 속한 모든 정수의 합 출력


def solution_001(a, b):
    a, b = sorted([a, b])

    # return sum([i for i in range(a, b + 1)]) if a != b else a
    return sum(range(a, b + 1))


def solution_002(a, b):
    # 가우스의 덧셈: n * (n + 1) // 2
    return (abs(a - b) + 1) * (a + b) // 2


# run result
a_001 = 5  # answer = 12
b_001 = 3
print(solution_001(a_001, b_001))
print(solution_002(a_001, b_001))

a_002 = 3  # answer = 3
b_002 = 3
print(solution_001(a_002, b_002))
print(solution_002(a_002, b_002))