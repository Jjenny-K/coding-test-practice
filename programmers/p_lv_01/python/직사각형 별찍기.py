# 가로 a, 세로 b인 직사각형 출력
from programmers.utils import set_input_number

# 두 개의 정수
a, b = set_input_number()


def solution_001(a, b):
    for _ in range(b):
        print("*" * a)


def solution_002(a, b):
    print(('*' * a + '\n') * b)


# run result
solution_001(a, b)
solution_002(a, b)