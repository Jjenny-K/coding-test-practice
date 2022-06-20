# 배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째 있는 수
# [i, j, k]를 원소로 가진 2차원 배열 commands에 연산을 적용했을 때 나온 결과를 배열에 담아 출력

def solution_001(array, commands):
    answer = []

    for val in commands:
        answer.append(sorted(array[val[0] - 1:val[1]])[val[2] - 1])

    print(answer)


def solution_002(array, commands):
    print(list(map(lambda x: sorted(array[x[0] - 1:x[1]])[x[2] - 1], commands)))


# run result
array_001 = [1, 5, 2, 6, 3, 7, 4]
commands_001 = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
solution_001(array_001, commands_001)
solution_002(array_001, commands_001)