# 완전 탐색 # 약수

# 각 기사 번호의 약수 개수에 해당하는 공격력을 가진 무기 구매
# 약수의 개수가 공격력 제한수치를 초과할 경우 제한된 공격력을 가진 무기 구매
# 공격력 1당 1kg의 철이 필요
# 기사단원 수 number, 공격력 제한수치 limit, 제한 공격력 power가 주어질 때, 무기를 모두 만들기 위한 철의 무게 출력


def get_divisor_cnt(n, limit, power):
    cnt = 0

    for j in range(1, int(n ** 0.5) + 1):
        if n % j == 0:
            if n // j == j:
                # 해당 약수가 제곱수일 경우
                cnt += 1
            else:
                cnt += 2

    if cnt > limit:
        return power

    return cnt


def solution(number, limit, power):
    answer = 1

    for i in range(2, number + 1):
        answer += get_divisor_cnt(i, limit, power)

    return answer


# run answer
number_001 = 10  # answer = 21
limit_001 = 3
power_001 = 2
print(solution(number_001, limit_001, power_001))