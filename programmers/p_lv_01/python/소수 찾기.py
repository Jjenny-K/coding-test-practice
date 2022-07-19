# 자연수 1 - n까지 소수의 개수 출력


def solution_001(n):
    answer = 0

    for i in range(2, n + 1):
        cnt = 0
        for j in range(2, i + 1):
            if i % j == 0:
                cnt += 1
        # 나누어 떨어진 횟수가 한 번뿐일 경우
        if cnt == 1:
            answer += 1

    return answer


def solution_002(n):
    answer = 0

    for i in range(2, n + 1):
        cnt = 0
        for j in range(2, (i // 2) + 1):
            if i % j == 0:
                cnt += 1
        # 나누어 떨어진 횟수가 없는 경우
        if cnt == 0:
            answer += 1

    return answer


def solution_003(n):
    # 에라토스테네스의 체: 범위내에서 합성수를 지우는 방식으로 소수 찾기
    answer = 0
    prime_list = [False, False, ] + [True] * (n - 1)

    for i in range(2, n + 1):
        if prime_list[i]:
            answer += 1
            for j in range(2 * i, n + 1, i):
                prime_list[j] = False

    return answer


def solution_004(n):
    num = set(range(2, n + 1))

    for i in range(2, n + 1):
        if i in num:
            num -= set(range(2 * i, n + 1, i))

    return len(num)


# run result
n_001 = 10  # answer = 4
print(solution_001(n_001))
print(solution_002(n_001))
print(solution_003(n_001))
print(solution_004(n_001))