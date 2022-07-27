# 행렬

# 행렬의 곱셈: 행렬 A의 열의 개수와 행렬 B의 행의 개수가 같을 때,
#            A의 i행 성분과 B의 j열 성분을 순서대로 곱해 더한 것을 (i, j)성분으로 하는 행렬
# 두 개의 행렬 arr1, arr2 곱셈 결과 출력


def solution_001(arr1, arr2):
    answer = []

    for i in arr1:
        tmp = []

        for j in zip(*arr2):
            tmp.append(sum([a * b for a, b in zip(i, j)]))

        answer.append(tmp)

    return answer


def solution_002(arr1, arr2):
    return [[sum(a * b for a, b in zip(A_row, B_col)) for B_col in zip(*arr2)] for A_row in arr1]


# run result
arr1_001 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]  # answer = [[22, 22, 11], [36, 28, 18], [29, 20, 14]]
arr2_001 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]
print(solution_001(arr1_001, arr2_001))
print(solution_002(arr1_001, arr2_001))