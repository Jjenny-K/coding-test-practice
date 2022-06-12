# x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트 출력
from programmers.utils import set_input_number

# 두 개의 정수
x, n = set_input_number()


def solution_001(x, n):
    answer = []
    for i in range(n):
        answer.append(x * (i + 1))
    print(answer)


def solution_002(x, n):
    print([x * (i + 1) for i in range(n)])


def solution_003(x, n):
    print(list(range(x, x * (n + 1), x)))


# run result
solution_001(x, n)
solution_002(x, n)
solution_003(x, n)