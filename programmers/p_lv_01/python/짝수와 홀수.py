# 수학 # 짝수 & 홀수

# 정수 num이 짝수일 경우 'Even', 홀수일 경우 'Odd' 출력


def solution_001(num):
    # return 'Even' if num % 2 == 0 else 'Odd'
    return 'Odd' if num % 2 else 'Even'


def solution_002(num):
    # 비트 연산자 &: 2진수로 나타낸 비트에서 둘 다 참일때 만족
    return ["Even", "Odd"][num & 1]


# run result
num_001 = 3  # answer = 'Odd'
print(solution_001(num_001))
print(solution_002(num_001))

num_002 = 4  # answer = 'Even'
print(solution_001(num_002))
print(solution_002(num_002))