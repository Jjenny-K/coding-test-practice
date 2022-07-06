# 두 정수 left에서 right까지 모든 수 중에서 약수의 개수가 짝수일 경우 더하고, 홀수일 경우 뺀 수 출력
# left <= right


def solution_001(left, right):
    answer = 0
    for i in range(left, right + 1):
        if (1 + len([j for j in range(1, (i // 2) + 1) if i % j == 0])) % 2 == 0:
            answer += i
        else:
            answer -= i

    print(answer)


def solution_002(left, right):
    # '제곱수의 약수는 홀수개이다' == '제곱근이 정수로 표현 가능하다면 약수의 개수는 홀수개이다'
    # n의 제곱근: n ** 0.5 == math.sqrt(n)
    answer = 0
    for i in range(left, right + 1):
        if int(i ** 0.5) == i ** 0.5:
            answer -= i
        else:
            answer += i

    print(answer)


# run result
left_001 = 24
right_001 = 27
solution_001(left_001, right_001)
solution_002(left_001, right_001)