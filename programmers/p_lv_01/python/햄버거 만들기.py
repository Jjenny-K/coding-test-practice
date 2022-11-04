# 완전 탐색 # stack

# 재료가 순서대로 아래에서 위로 쌓이고, (아래부터)'빵-야채-고기-빵'으로 쌓였을 때 포장
# 재료 정보 배열 ingredient가 주어질 때, 포장가능한 햄버거의 개수 출력


def solution_001(ingredient):
    answer = 0
    buger_stack = []

    for value in ingredient:
        buger_stack.append(value)

        if len(buger_stack) >= 4 and buger_stack[-4:] == [1, 2, 3, 1]:
            answer += 1

            for _ in range(4):
                buger_stack.pop()

    return answer


def solution_002(ingredient):
    ingredient = "".join(list(map(str, ingredient)))

    if len(ingredient) < 4:
        return 0

    answer = 0
    buger_stack = ingredient[:3]

    for value in ingredient[3:]:
        buger_stack += value

        if buger_stack[-4:] == "1231":
            answer += 1
            buger_stack = buger_stack[:-4]

    return answer


# run result
ingredient_001 = [2, 1, 1, 2, 3, 1, 2, 3, 1]  # answer = 2
print(solution_001(ingredient_001))
print(solution_002(ingredient_001))

ingredient_002 = [1, 3, 2, 1, 2, 1, 3, 1, 2]  # answer = 0
print(solution_001(ingredient_002))
print(solution_002(ingredient_002))