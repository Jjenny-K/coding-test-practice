# 수학 # 순열 & 조합

# 각자 정수 번호를 가진 학생들 중 3명의 정수 번호를 더했을 때 0이 되면 해당 3명은 삼총사
# 정수 배열이 주어질 때, 삼총사를 만들 수 있는 방법의 수 출력
import itertools


def solution_001(number):
    # combinations 사용해 3가지를 선택할 수 있는 조합 파악
    number_combinations = list(itertools.combinations(number, 3))

    answer = 0

    for value in number_combinations:
        if sum(value) == 0:
            # 정수 번호의 합이 0이라면
            answer += 1

    return answer


def solution_002(number):
    return len([case for case in itertools.combinations(number, 3) if sum(case) == 0])


# run result
number_001 = [-3, -2, -1, 0, 1, 2, 3]  # answer = 5
print(solution_001(number_001))
print(solution_002(number_001))

number_002 = [-1, 1, -1, 1]  # answer = 0
print(solution_001(number_002))
print(solution_002(number_002))