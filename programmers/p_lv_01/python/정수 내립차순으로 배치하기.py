# 정수 n의 각 자릿수를 내림차순으로 정렬한 새로운 정수 출력


def solution(n):
    return int(''.join(sorted(str(n), reverse=True)))


# run result
n_001 = 118372  # answer = 873211
print(solution(n_001))