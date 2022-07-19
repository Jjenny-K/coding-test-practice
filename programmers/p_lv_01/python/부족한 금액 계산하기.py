# 놀이기구 이용료 price, n번째 이용할 경우 이용료의 n배
# 놀이기구를 count번 탈 경우 부족한 금액 출력
# 금액이 부족하지 않을 경우 0 출력


def solution_001(price, money, count):
    answer = sum([price * i for i in range(1, count + 1)]) - money

    return answer if answer > 0 else 0


def solution_002(price, money, count):
    # 등차수열 합: x * n * (n + 1) // 2
    return max(0, (price * count * (count + 1) // 2) - money)


def solution_003(price, money, count):
    # return abs(min(money - sum([price * i for i in range(1, count + 1)]), 0))
    return max(sum([price * i for i in range(1, count + 1)]) - money, 0)


# run result
price_001 = 3  # answer = 10
money_001 = 20
count_001 = 4
print(solution_001(price_001, money_001, count_001))
print(solution_002(price_001, money_001, count_001))
print(solution_003(price_001, money_001, count_001))