# 백트래킹

# 스도쿠의 빈칸 채우기

import sys

sudoku, blank = [], []

for i in range(9):
    sudoku.append(list(map(int, sys.stdin.readline().split())))
    for j in range(9):
        if sudoku[i][j] == 0:
            blank.append([i, j])


def chk_row(x, n):
    for i in range(9):
        if sudoku[x][i] == n:
            # 같은 행에 n이 있을 경우 False
            return False

    return True


def chk_col(y, n):
    for i in range(9):
        if sudoku[i][y] == n:
            # 같은 열에 n이 있을 경우 False
            return False

    return True


def chk_rect(x, y, n):
    nx = x // 3 * 3
    ny = y // 3 * 3

    for i in range(3):
        for j in range(3):
            if sudoku[nx + i][ny + j] == n:
                # 일정 3x3 구역 내에 n이 있을 경우 False
                return False

    return True


def solution_sudoku(idx):
    if idx == len(blank):
        for _ in range(9):
            print(*sudoku[_])
        exit(0)

    x, y = blank[idx]

    for i in range(1, 10):
        if chk_row(x, i) and chk_col(y, i) and chk_rect(x, y, i):
            sudoku[x][y] = i  # 행, 열, 일정 구역 내에 i가 없을 경우 해당 위치에 대입
            solution_sudoku(idx + 1)
            sudoku[x][y] = 0  # 답이 완성되지 않았을 경우 대비


solution_sudoku(0)