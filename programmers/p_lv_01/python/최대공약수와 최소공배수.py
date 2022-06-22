"""
    최대공약수: GCD, 두 수 혹은 그 이상의 여러 수의 공통인 약수 중 최대인 것
    최소공배수: LCM, 두 수 혹은 그 이상의 여러 수의 공통인 배수 중 최소인 것
"""
# 두 자연수의 최대공약수, 최소공배수 출력
import math


def solution_001(n, m):
    answer = []

    # 두 수를 나누어 나머지가 0일 경우 최대공약수
    for i in range(min(n, m), 0, -1):
        if (n % i == 0) & (m % i == 0):
            answer.append(i)
            break

    # 두 수로 나누어 나머지가 0일 경우 최소공배수
    for j in range(max(n, m), (n * m) + 1):
        if (j % n == 0) & (j % m == 0):
            answer.append(j)
            break

    print(answer)


def solution_002(n, m):

    def get_gcd(x, y):
        # 유클리드 호제법: x, y의 최대 공약수는 y, r의 최대 공약수와 같다, x % y = r
        return y if x % y == 0 else get_gcd(y, x % y)

    def get_lcm(x, y):
        # 두 수를 곱한 값을 최대공약수로 나눈 몫은 최소공배수이다
        return (x * y) // get_gcd(x, y)

    print([get_gcd(n, m), get_lcm(n, m)])


def solution_003(n, m):
    print([math.gcd(n, m), math.lcm(n, m)])


# run result
n_001 = 3
m_001 = 12
solution_001(n_001, m_001)
solution_002(n_001, m_001)
solution_003(n_001, m_001)