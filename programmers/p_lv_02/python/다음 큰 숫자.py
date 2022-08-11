# 수학 # 2진법

# 자연수 n이 주어질 때, n보다 크고, 2진법으로 변환했을 때 1의 갯수가 같은 수 중 가장 작은 수 출력

def solution(n):
    cnt_n_one = bin(n)[2:].count('1')

    while True:
        n += 1
        if bin(n)[2:].count('1') == cnt_n_one:
            break

    return n


# run result
n_001 = 78  # answer = 83
print(solution(n_001))