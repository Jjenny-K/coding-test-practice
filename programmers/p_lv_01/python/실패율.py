# 게임의 실패율 구하기
# 실패율: 스테이지에 도달했으나 아직 클리어하지 못한 플레이어 수 / 스테이지에 도달한 플레이어 수
# 전체 스테이지 수 N, 플레이어들이 멈춰있는 스테이지 번호가 담긴 배열 stages
# 실패율이 높은 스테이지부터 내림차순으로 스테이지 번호가 담겨있는 배열 출력
# 실패율이 같은 스테이지는 작은 번호의 스테이지가 먼저 오도록 출력
import collections


def solution_001(N, stages):
    answer = []
    users = len(stages)

    for i in range(1, N + 1):
        failure = 0

        for k, v in sorted(collections.Counter(stages).items()):
            if i == k:
                failure = v / users
                users -= v
                break

        answer.append((i, failure))

    return [i[0] for i in sorted(answer, key=lambda x: (-x[1], x[0]))]


def solution_002(N, stages):
    result = {}
    denominator = len(stages)

    for stage in range(1, N + 1):

        if denominator != 0:
            count = stages.count(stage)
            result[stage] = count / denominator
            denominator -= count
        else:
            result[stage] = 0

    return sorted(result, key=lambda x: result[x], reverse=True)


def solution_003(N, stages):
    fail = {}

    for i in range(1, N + 1):
        try:
            fail_ = len([a for a in stages if a == i]) / len([a for a in stages if a >= i])
        except:
            fail_ = 0

        fail[i] = fail_

    return sorted(fail, key=fail.get, reverse=True)


def solution_004(N, stages):
    answer = []
    fail = []
    info = [0] * (N + 2)

    for stage in stages:
        info[stage] += 1

    for i in range(N):
        be = sum(info[(i + 1):])
        yet = info[i + 1]

        if be == 0:
            fail.append((str(i + 1), 0))
        else:
            fail.append((str(i + 1), yet / be))

    for item in sorted(fail, key=lambda x: x[1], reverse=True):
        answer.append(int(item[0]))

    return answer


# run result
N_001 = 5  # answer = [3, 4, 2, 1, 5]
stages_001 = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution_001(N_001, stages_001))
print(solution_002(N_001, stages_001))
print(solution_003(N_001, stages_001))
print(solution_004(N_001, stages_001))