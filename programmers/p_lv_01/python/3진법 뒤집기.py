# 수학 # n진법

# 자연수 n을 3진법 상에서 앞뒤로 뒤집은 후 다시 10진법으로 표현한 수 출력
import string


def solution_001(n):
    def convert(num, base):
        tmp = string.digits + string.ascii_lowercase  # 0123456789abcdefghijklmnopqrstuvwxyz
        q, r = divmod(num, base)

        if q == 0:
            return tmp[r]
        else:
            return convert(q, base) + tmp[r]

    return int(convert(n, 3)[::-1], 3)


def solution_002(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    return int(tmp, 3)


# run result
n_001 = 125  # answer = 229
print(solution_001(n_001))
print(solution_002(n_001))