# 0 - 9로 이루어진 배열에서 연속적으로 나타나는 숫자를 하나만 남기고 제거한 배열 출력

def solution_001(arr):
    answer = [arr[0]]

    for val in arr[1:]:
        if answer[-1] != val:
            answer.append(val)

    return answer


def solution_002(arr):
    answer = []

    for val in arr:
        if answer[-1:] != [val]:
            answer.append(val)

    return answer


# run result
arr_001 = [1, 1, 3, 3, 0, 1, 1]  # answer = [1, 3, 0, 1]
print(solution_001(arr_001))
print(solution_002(arr_001))