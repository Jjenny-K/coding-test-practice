# 로또 당첨이 가능했던 최고 순위와 최저 순위 출력
# 구매한 로또 번호를 담은 배열 lottos, 당첨 번호를 담은 배열 win_nums
# 알아볼 수 없는 번호는 0으로 표기


def solution_001(lottos, win_nums):
    win_cnts = 0

    for i in lottos:
        if i > 0 and i in win_nums:
            win_cnts += 1

    if win_cnts == 0:
        if lottos.count(0) == 0:
            return 6, 6
        else:
            return 1, 6
    elif win_cnts == 6:
        return 1, 1
    else:
        return 7 - (lottos.count(0) + win_cnts), 7 - win_cnts if win_cnts >= 2 else 6


def solution_002(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]

    # win_cnts = 0
    # for x in win_nums:
    #     if x in lottos:
    #         win_cnts += 1
    #
    # return rank[lottos.count(0) + win_cnts], rank[win_cnts]

    return rank[len(set(lottos) & set(win_nums)) + lottos.count(0)], rank[len(set(lottos) & set(win_nums))]


# run result
lottos_001 = [0, 0, 0, 0, 0, 0]  # answer = (1, 6)
win_nums_001 = [38, 19, 20, 40, 15, 25]
print(solution_001(lottos_001, win_nums_001))
print(solution_002(lottos_001, win_nums_001))

lottos_002 = [45, 4, 35, 20, 3, 9]  # answer = (1, 1)
win_nums_002 = [20, 9, 3, 45, 4, 35]
print(solution_001(lottos_002, win_nums_002))
print(solution_002(lottos_002, win_nums_002))