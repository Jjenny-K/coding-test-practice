# 완전 탐색 # min

# 매일 출연 가수의 점수를 상위 k번째 이내일 경우 명에의 전당에 기록, 최하위 점수 발표
# 명에의 전당 목록 점수의 개수 k, 매일 출연한 가수둘의 점수 score가 주이질 때, 발표된 최하위 점수 출력


def solution(k, score):
    fame = []
    answer = []

    for value in score:
        fame.append(value)

        if len(fame) > k:
            fame.remove(min(fame))

        answer.append(min(fame))

    return answer


# run result
k_001 = 4  # answer = [0, 0, 0, 0, 20, 40, 70, 70, 150, 300]
score_001 = [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]
print(solution(k_001, score_001))