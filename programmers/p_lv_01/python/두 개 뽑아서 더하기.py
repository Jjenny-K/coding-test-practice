# 정수 배열 numbers에서 서로 다른 인덱스에 있는 두개의 수를 뽑아 더해서 만들 수 있는 모든 수 배열에 담아 출력
import itertools


def solution_001(numbers):
    return sorted(set([sum(i) for i in list(itertools.combinations(numbers, 2))]))


def solution_002(numbers):
    answer = []

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            answer.append(numbers[i] + numbers[j])

    return sorted(set(answer))


# run result
numbers_001 = [2, 1, 3, 4, 1]  # answer = [2, 3, 4, 5, 6, 7]
print(solution_001(numbers_001))
print(solution_002(numbers_001))