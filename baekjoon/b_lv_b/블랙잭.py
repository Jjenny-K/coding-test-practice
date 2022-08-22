# 브루드 포스

# 블랙잭 : 카드의 합이 21을 넘지 않는 한도 내에서 카드 합을 최대한으로 만드는 게임
# n장의 카드가 놓여지고 숫자 m이 주아질 때, 놓여진 카드 중 3장을 골라 m을 넘지 않으면서 m에 최대한 가까운 합 출력

import itertools

card_cnt, target = map(int, input().split())
cards = list(map(int, input().split()))

answer = 0

for case in itertools.combinations(cards, 3):
    tmp = sum(case)

    if answer < tmp <= target:
        answer = tmp

print(answer)