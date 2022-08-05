# 수학 # 연산 # aver

# 정수 배열 arr 평균값 출력

def solution(arr):
    if len(arr) == 0:
        return 0
    else:
        return sum(arr) / len(arr)


# run result
arr_001 = [1, 2, 3, 4]  # answer = 2.5
print(solution(arr_001))

arr_002 = []  # answer = 0
print(solution(arr_002))