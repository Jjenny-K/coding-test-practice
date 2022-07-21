# 연산

# 하샤드 수: 양의 정수 x가 자릿수의 합으로 x가 나누어질 경우 정수 x
# 자연수 x가 하샤드 수인지 아닌지 출력

def solution_001(x):
    answer = True
    if x % sum(map(int, str(x))) != 0:
        answer = False

    return answer

    # return False if x % sum(map(int, str(x))) != 0 else True


def solution_002(x):
    return x % sum([int(i) for i in str(x)]) == 0


# run result
x_001 = 11  # answer = False
print(solution_001(x_001))
print(solution_002(x_001))

x_002 = 18  # answer = True
print(solution_001(x_002))
print(solution_002(x_002))