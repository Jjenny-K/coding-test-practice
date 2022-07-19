# 길이가 같은 1차원 정수 배열 a, b의 내적 출력
# 내적: a[0]*b[0] + a[1]*b[1] + ... + a[n-1]*b[n-1](스칼라 곱..?)


def solution_001(a, b):
    return sum([i * j for i, j in zip(a, b)])


def solution_002(a, b):
    return sum(list(map(lambda x, y: x * y, a, b)))


# run result
a_001 = [1, 2, 3, 4]  # answer = 3
b_001 = [-3, -1, 0, 2]
print(solution_001(a_001, b_001))
print(solution_002(a_001, b_001))