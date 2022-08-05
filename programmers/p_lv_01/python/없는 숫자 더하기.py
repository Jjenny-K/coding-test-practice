# 자료 구조 # list

# 0 - 9 중 일부로 이루어진 배열 numbers에서 0 - 9 중 없는 수를 찾아서 더해 출력

def solution_001(numbers):
    return sum(list(range(0, 10))) - sum(set(numbers))


def solution_002(numbers):
    return sum([i for i in list(range(0, 10)) if i not in numbers])


# run result
numbers_001 = [5, 8, 4, 0, 6, 7, 9]  # answer = 6
print(solution_001(numbers_001))
print(solution_002(numbers_001))