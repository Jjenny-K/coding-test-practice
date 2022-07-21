# 완전탐색 # list

# 수포자 3명, 정답이 순서대로 들은 배열 answers에서 가장 많은 문제를 맞힌 사람을 배열로 출력
# 가장 많은 문제를 맞힌 사람이 여럿일 경우 오름차순 정렬
"""
    수포자의 찍는 방식
    1번 수포자: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
    2번 수포자: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
    3번 수포자: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...
"""


def solution_001(answers):
    answer = {x: 0 for x in range(1, 4)}

    stu_a = [1, 2, 3, 4, 5]
    stu_b = [2, 1, 2, 3, 2, 4, 2, 5]
    stu_c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    stu_a = stu_a * (10000 // len(stu_a))
    stu_b = stu_b * (10000 // len(stu_b))
    stu_c = stu_c * (10000 // len(stu_c))

    for idx, value in enumerate(answers):
        if value == stu_a[idx]:
            answer[1] += 1
        if value == stu_b[idx]:
            answer[2] += 1
        if value == stu_c[idx]:
            answer[3] += 1

    return [key for key, value in answer.items() if value == max(answer.values())]


def solution_002(answers):
    stu_a = [1, 2, 3, 4, 5]
    stu_b = [2, 1, 2, 3, 2, 4, 2, 5]
    stu_c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]

    for idx, answer in enumerate(answers):
        if answer == stu_a[idx % len(stu_a)]:
            score[0] += 1
        if answer == stu_b[idx % len(stu_b)]:
            score[1] += 1
        if answer == stu_c[idx % len(stu_c)]:
            score[2] += 1

    return [idx + 1 for idx, value in enumerate(score) if value == max(score)]


# run result
answers_001 = [1, 3, 2, 4, 2]  # answer = [1, 2, 3]
print(solution_001(answers_001))
print(solution_002(answers_001))