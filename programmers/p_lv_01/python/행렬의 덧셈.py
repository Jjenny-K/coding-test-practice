# 행렬의 덧셈: 행과 열의 크가가 같은 두 행렬의 같은 행, 같은 열 값을 서로 더한 결과
# 두 개의 행렬 arr1, arr2 덧셈 결과 출력

def solution_001(arr1, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            arr1[i][j] += arr2[i][j]
    print(arr1)


def solution_002(arr1, arr2):
    print([[c + d for c, d in zip(a, b)] for a, b in zip(arr1, arr2)])


# run result
arr1_001 = [[1,2],[2,3]]
arr2_001 = [[3,4],[5,6]]
solution_001(arr1_001, arr2_001)
solution_002(arr1_001, arr2_001)