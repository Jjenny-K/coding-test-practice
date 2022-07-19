# x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트 출력
from programmers.utils import set_input_number

# 두 개의 정수
x_001, n_001 = set_input_number()


def solution_001(x, n):
    answer = []

    for i in range(n):
        answer.append(x * (i + 1))

    return answer


def solution_002(x, n):
    return [x * (i + 1) for i in range(n)]


def solution_003(x, n):
    return list(range(x, x * (n + 1), x))


# run result
print(solution_001(x_001, n_001))
print(solution_002(x_001, n_001))
print(solution_003(x_001, n_001))