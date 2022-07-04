# 부서별 필요한 물품 구매 신청 금액 배열 d, 에산 budget이 주어질 때, 최대 몇개의 부서에 지원 가능한지 출력
# 물품 구매 시 신청한 금액을 전부 지원해 줄 수 있어야함


def solution_001(d, budget):
    d.sort()

    for _ in range(len(d)):
        if sum(d) > budget:
            d.pop()

    print(len(d))


def solution_002(d, budget):
    answer = 0

    for i in sorted(d):
        if budget < 0:
            break
        budget -= i
        answer += 1

    print(answer)


# run result
d_001 = [1, 3, 2, 5, 4]
budget_001 = 9
solution_001(d_001, budget_001)
solution_002(d_001, budget_001)