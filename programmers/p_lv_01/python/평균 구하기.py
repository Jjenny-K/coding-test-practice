# 정수 배열 arr 평균값 출력

def solution(arr):
    if len(arr) == 0:
        print(0)
    else:
        print(sum(arr) / len(arr))


# run result
arr_001 = [1, 2, 3, 4]
solution(arr_001)

arr_002 = []
solution(arr_002)