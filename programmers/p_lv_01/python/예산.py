# 탐색 # 탐욕법

# 부서별 필요한 물품 구매 신청 금액 배열 d, 에산 budget이 주어질 때, 최대 몇개의 부서에 지원 가능한지 출력
# 물품 구매 시 신청한 금액을 전부 지원해 줄 수 있어야함


def solution_001(d, budget):
    d.sort()

    for _ in range(len(d)):
        if sum(d) > budget:
            d.pop()

    return len(d)


def solution_002(d, budget):
    answer = 0

    for i in sorted(d):
        if budget < 0:
            break
        budget -= i
        answer += 1

    return answer


# run result
d_001 = [1, 3, 2, 5, 4]  # answer = 3
budget_001 = 9
print(solution_001(d_001, budget_001))
print(solution_002(d_001, budget_001))