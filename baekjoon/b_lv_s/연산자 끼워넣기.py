# 브루트 포스 # 백트래킹

# N개의 수로 이루어진 수열, N-1개의 연산자(덧셈, 뺄셈, 곱셈, 나눗셈 순의 연산자 개수 리스트)
# 음수를 양수로 나눌 때는 수를 양수로 바꾸어 몫을 취하고 그 몫을 음수로 바꿈
# 수와 수 사이에 연산자를 하나씩 끼워 넣어 수식을 만들었을 때, 결과가 최대인 것과 최소인 것 출력

N = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))  # +, -, *, // 순서

maximum, minimum = -1e9, 1e9  # 가장 작은 수, 큰 수로 maximum, minimum 초기화


def calculation(cnt, total, plus, minus, multiply, divide):
    global maximum, minimum

    if cnt == N:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return

    if plus:
        calculation(cnt + 1, total + numbers[cnt], plus - 1, minus, multiply, divide)
    if minus:
        calculation(cnt + 1, total - numbers[cnt], plus, minus - 1, multiply, divide)
    if multiply:
        calculation(cnt + 1, total * numbers[cnt], plus, minus, multiply - 1, divide)
    if divide:
        if total < 0:
            # 분모가 음수일 경우, 분모를 양수로 바꾼 뒤 나눗셈의 몫을 음수로 변경
            calculation(cnt + 1, -(abs(total) // numbers[cnt]), plus, minus, multiply, divide - 1)
        else:
            calculation(cnt + 1, total // numbers[cnt], plus, minus, multiply, divide - 1)


calculation(1, numbers[0], operators[0], operators[1], operators[2], operators[3])
print(maximum, minimum, sep='\n')