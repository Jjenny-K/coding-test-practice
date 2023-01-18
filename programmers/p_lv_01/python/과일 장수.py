# 완전 탐색 # list

# 사과의 상품 점수 1점 - k점, 한 상자의 포장 개수 m개
# 한 상자의 가격 = 상자 내 가장 낮은 사과의 점수 * m
# 사과들의 점수 배열 score가 주어질 때, 과일 장수가 얻을 수 있는 최대 이익 출력


def solution_001(k, m, score):
    answer = 0

    score = sorted(score)[::-1]
    split_box = [score[i * m:m * (i + 1)] \
                 for i in range(0, (len(score) + m - 1) // m)]

    for value in split_box:
        if len(value) == m:
            answer += value[-1] * m

    return answer


def solution_002(k, m, score):
    return sum(sorted(score)[len(score) % m::m]) * m


# run result
k_001 = 3  # answer = 8
m_001 = 4
score_001 = [1, 2, 3, 1, 2, 3, 1]
print(solution_001(k_001, m_001, score_001))
print(solution_002(k_001, m_001, score_001))

k_002 = 4  # answer = 33
m_002 = 3
score_002 = [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]
print(solution_001(k_002, m_002, score_002))
print(solution_002(k_002, m_002, score_002))