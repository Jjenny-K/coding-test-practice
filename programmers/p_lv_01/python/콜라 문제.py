# 수학 # 연산 # max

# 빈 병 a개를 가져다주면 콜라 b병을 주는 마트가 있을 때, 빈 병 n개를 가져다주면 받을 수 있는 콜라의 개수 출력
# 보유 중인 빈 병이 a개 미만일 경우 추가 빈 병을 받을 수 없음


def solution_001(a, b, n):
    answer = 0

    while n >= a:
        get_coke = (n // a) * b
        answer += get_coke
        n = get_coke + (n % a)

    return answer


def solution_002(a, b, n):
    return max(n - b, 0) // (a - b) * b


# run result
a_001 = 3  # answer = 9
b_001 = 1
n_001 = 20
print(solution_001(a_001, b_001, n_001))
print(solution_002(a_001, b_001, n_001))

a_002 = 3  # answer = 36
b_002 = 2
n_002 = 20
print(solution_001(a_002, b_002, n_002))
print(solution_002(a_002, b_002, n_002))