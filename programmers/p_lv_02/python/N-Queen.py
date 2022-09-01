# 탐색 # 백트래킹

# 크기가 n x n인 체스판이 주어질 때, 퀸 n개를 서로 공격할 수 없게 배치할 수 있는 방법의 수 출력

def solution(n):
    return n_queens([0] * n, n, 0)


def n_queens(queens, n, row):
    cnt = 0

    if n == row:
        return 1

    for col in range(n):
        queens[row] = col

        for i in range(row):
            # 세로로 겹치거나 대각선으로 겹칠 경우 break
            if (queens[i] == queens[row]) or (abs(queens[i] - queens[row]) == abs(row - i)):
                break
        else:
            cnt += n_queens(queens, n, row + 1)

    return cnt


# run result
n_001 = 4  # answer = 2
print(solution(n_001))