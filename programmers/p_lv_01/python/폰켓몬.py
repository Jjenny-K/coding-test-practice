# 탐색 # 탐욕법

# 연구실에 있는 총 N마리의 폰켓몬 중 N/2마리를 가져갈 수 있을 때, 폰켓몬 종류 nums 중 가장 많은 종류의 폰켓몬을 선택하는 방법 출력


def solution_001(nums):
    return len(nums) // 2 if (len(nums) // 2) <= len(set(nums)) else len(set(nums))


def solution_002(nums):
    return min((len(nums) // 2), len(set(nums)))


# run result
nums_001 = [3, 1, 2, 3]  # answer = 2
print(solution_001(nums_001))
print(solution_002(nums_001))

nums_002 = [3, 3, 3, 2, 2, 2]  # answer = 2
print(solution_001(nums_002))
print(solution_002(nums_002))