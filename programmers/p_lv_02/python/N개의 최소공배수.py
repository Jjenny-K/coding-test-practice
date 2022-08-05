# 수학 # 최대공약수 & 최소공배수

# n개의 수 최소공배수: n개의 수들의 배수 중 공통이 되는 가장 작은 숫자
# n개의 숫자를 담은 배열 arr에서 arr 내 수들의 최소공배수 출력
import math


def solution_001(arr):
    def get_gcd(x, y):
        return y if x % y == 0 else get_gcd(y, x % y)

    def get_lcm(x, y):
        return (x * y) // get_gcd(x, y)

    answer = arr[0]

    for i in range(1, len(arr)):
        answer = get_lcm(answer, arr[i])

    return answer


def solution_002(arr):
    answer = arr[0]

    for n in arr:
        answer = (answer * n) // math.gcd(n, answer)

    return answer


# run result
arr_001 = [2, 6, 8, 14]  # answer = 168
print(solution_001(arr_001))
print(solution_002(arr_001))