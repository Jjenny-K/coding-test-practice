# 브루트 포스 # 백트래킹

# 크기가 N x N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 방법의 수 출력

size = int(input())

row = [0] * size
cnt = 0


def n_queens(x):
    global cnt

    if x == size:
        # size에 맞춰서 모든 위치에 적절하게 queen이 놓여진다면 cnt + 1
        cnt += 1
    else:
        for y in range(size):
            # queen 위치를 [x, y]라고 생각했을 때,
            row[x] = y

            if is_located(x):
                n_queens(x + 1)


def is_located(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            # 세로로 같은 위치에 놓여지거나, 오른편 대각선 위치에 놓여진다면 False
            return False
    else:
        return True


n_queens(0)
print(cnt)