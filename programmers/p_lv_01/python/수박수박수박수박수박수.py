# 길이가 n인 '수박수박수박수박수...' 패턴을 유지하는 문자열 출력


def solution_001(n):
    answer = ''

    for i in range(n):
        if i % 2 == 0:
            answer += '수'
        else:
            answer += '박'

    print(answer)


def solution_002(n):
    print("".join(["수박"[i % 2] for i in range(n)]))


def solution_003(n):
    print("수박" * (n // 2) + "수" * (n % 2))


# run result
n_001 = 17
solution_001(n_001)
solution_002(n_001)
solution_003(n_001)