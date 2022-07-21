# min # list

# 정수 배열 arr 가장 작은 수 제거한 배열 출력
# 출력할 배열이 빈 배열인 경우 -1 채워 출력

def solution(arr):
    arr.remove(min(arr))

    if len(arr) == 0:
        arr.append(-1)

    return arr


# run result
arr_001 = [1, 4, 3, 2]  # answer = [4, 3, 2]
print(solution(arr_001))

arr_002 = [10]  # answer = [-1]
print(solution(arr_002))