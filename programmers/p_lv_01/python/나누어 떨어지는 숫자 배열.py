# 배열 각 원소 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열 출력
# 출력할 배열이 빈 배열인 경우 -1 채워 출력

def solution_001(arr, divisor):
    answer = [i for i in arr if i % divisor == 0]
    answer.sort()

    if len(answer) == 0:
        answer.append(-1)

    return answer


def solution_002(arr, divisor):
    answer = sorted([i for i in arr if i % divisor == 0])

    return answer if len(answer) != 0 else [-1]


def solution_003(arr, divisor):
    return sorted([i for i in arr if i % divisor == 0]) or [-1]


# run result
arr_001 = [5, 9, 7, 10]  # answer = [5, 10]
divisor_001 = 5
print(solution_001(arr_001, divisor_001))
print(solution_002(arr_001, divisor_001))
print(solution_003(arr_001, divisor_001))