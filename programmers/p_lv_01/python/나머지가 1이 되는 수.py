# 연산 # min

# 자연수 n을 x로 나눈 나머지가 1이 되도록 하는 가장 작은 자연수 x 출력


def solution_001(n):
    return min([i for i in range(1, n) if n % i == 1])


def solution_002(n):
    answer = 0

    for d in range(2, ((n - 1) // 2) + 1):  # 2부터 반값까지
        if (n - 1) % d == 0:  # (n - 1)의 약수가 있다면
            answer = d
            break  # 탈출
        else:
            answer = n - 1  # 약수가 없다면 (n - 1)

    return answer


# run result
n_001 = 10  # answer = 3
print(solution_001(n_001))
print(solution_002(n_001))