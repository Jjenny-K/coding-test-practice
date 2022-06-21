"""
    콜라츠 추측: Collatz에 의해 제기된 추측, 주어진 수가 1이 될 때까지 다음 작업을 반복할 경우 모든 수는 1이 된다.
    1.  입력된 수가 짝수라면 2로 나눈다.
        입력된 수가 홀수라면 3을 곱하고 1을 더한다.
    2. 결과로 나온 수에 같은 작업을 1이 될 때까지 반복한다.
"""
# 주어진 정수 num이 1이 될 때까지 작업이 반복되는 횟수 출력
# 주어진 정수가 1인 경우 0, 작업을 500번 반복할 때까지 1이 되지 않는다면 -1 출력


def solution(num):
    answer = 0
    count = 0

    while count < 500:
        if num == 1:
            break

        if num % 2 == 0:
            num = int(num / 2)
        else:
            num = int((num * 3) + 1)

        answer += 1
        count += 1

    print(-1 if answer >= 500 else answer)


# run result
num_001 = 16
solution(num_001)

num_002 = 1
solution(num_002)

num_003 = 626331
solution(num_003)