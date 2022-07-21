# list

# 자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 출력

def solution_001(n):
    # return list(map(int, reversed(str(n))))
    return list(map(int, str(n)))[::-1]


def solution_002(n):
    # return [int(i) for i in reversed(str(n))]
    return [int(i) for i in str(n)[::-1]]


# run result
n_001 = 12345  # answer = [5, 4, 3, 2, 1]
print(solution_001(n_001))
print(solution_002(n_001))