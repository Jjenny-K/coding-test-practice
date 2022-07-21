# dictionary

# 마라톤에 참여한 선수들 이름이 담긴 배열 participant, 완주한 선수들 이름이 담긴 배열 completion
# 완주하지 못한 선수의 이름 출력
# 참여한 선수들 중 동명이인이 있을 수 있음
import collections


def solution_001(participant, completion):
    participant.sort()
    completion.sort()

    # 정렬된 두 배열을 인덱스 순서대로 비교
    for p, c in zip(participant, completion):
        if p != c:
            return p

    return participant.pop()


def solution_002(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)

    return list(answer)[0]


# run result
participant_001 = ["leo", "kiki", "eden"]  # answer = 'leo'
completion_001 = ["eden", "kiki"]
print(solution_001(participant_001, completion_001))
print(solution_002(participant_001, completion_001))

participant_002 = ["mislav", "stanko", "mislav", "ana"]  # answer = 'mislav'
completion_002 = ["stanko", "ana", "mislav"]
print(solution_001(participant_002, completion_002))
print(solution_002(participant_002, completion_002))