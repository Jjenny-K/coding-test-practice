# 완전 탐색 # 문자열 출력

# 칼로리가 적은 순서대로 준비된 음식을 두 사람이 공평하게 같은 순서로 먹을 수 있도록 배치
# 중앙에는 가장 칼로리가 적은 물 배치(0번 음식)
# 준비한 음식 배열 food가 주어질 때, 대회를 위한 음식 배치 출력


def solution(food):
    contest_food = ''

    for idx, value in enumerate(food[1:], start=1):
        chk_used = value // 2

        if chk_used != 0:
            contest_food += str(idx) * chk_used

    return contest_food + '0' + contest_food[::-1]


# run result
food_001 = [1, 3, 4, 6]  # answer = '1223330333221'
print(solution(food_001))

food_002 = [1, 7, 1, 2]  # answer = '111303111'
print(solution(food_002))