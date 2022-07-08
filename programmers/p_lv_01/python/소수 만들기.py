# 숫자들이 들어있는 배열 nums에서 서로 다른 3개의 숫자를 골라 더했을 때 소수가 되는 경우의 수 출력
# 1 <= nums 내 원소 <= 1000
import itertools
import math


def solution_001(nums):
    answer = 0

    sum_list = [sum(i) for i in list(itertools.combinations(nums, 3))]

    for v in sum_list:
        chk = True
        for i in range(2, int(math.sqrt(v) + 1)):
            if v % i == 0:
                chk = False
        if chk:
            answer += 1

    print(answer)


def solution_002(nums):
    # 에라토스테네스의 체 이용
    def find_prime(n):
        if n < 2:
            return []

        p = [0, 0] + [1] * (n - 1)

        for i in range(2, int(n ** .5) + 1):
            if p[i]:
                p[i * 2::i] = [0] * ((n - i) // i)
        return [i for i, v in enumerate(p) if v]

    # 원소 중 가장 큰 수가 1000일 수 있고
    # 그를 포함해 3개를 골라 더했을 때 가장 클 경우가 3000 언저리
    prime_list = find_prime(3000)
    sum_list = [sum(i) for i in list(itertools.combinations(nums, 3))]

    print(len([v for v in sum_list if v in prime_list]))


# run result
nums_001 = [1, 2, 7, 6, 4]
solution_001(nums_001)
solution_002(nums_001)