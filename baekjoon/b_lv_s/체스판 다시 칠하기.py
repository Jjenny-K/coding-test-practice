# 브루트 포스

# 단위 정사각형으로 나뉘어 있는 MxN 크기의 보드에 어떤 정사각형은 검은색, 나머지는 흰색으로 칠해져 있을 때, 보드를 8x8 크기의 체스판으로 제작
# 체스판은 검은색과 흰색이 번갈아 칠해져 있어야하며 맨 왼쪽 위 칸이 흰색인 경우, 검은색인 경우 두 가지로 칠할 수 있음
# 주어진 보드에서 8x8 크기의 체스판을 만들 때 다시 칠해야하는 정사각형의 최소 개수 출력

def check_color(matrix):
    start_white, start_black = 0, 0

    # 맨 왼쪽 위 칸을 흰색으로 칠할 경우
    for x in range(8):
        for y in range(8):
            if (x % 2 == 0 and y % 2 == 0) or (x % 2 == 1 and y % 2 == 1):
                if matrix[x][y] != 'W':
                    start_white += 1
            else:
                if matrix[x][y] != 'B':
                    start_white += 1

    # 맨 왼쪽 위 칸을 검은색으로 칠할 경우
    for x in range(8):
        for y in range(8):
            if (x % 2 == 0 and y % 2 == 0) or (x % 2 == 1 and y % 2 == 1):
                if matrix[x][y] != 'B':
                    start_black += 1
            else:
                if matrix[x][y] != 'W':
                    start_black += 1

    return min(start_white, start_black)


M, N = map(int, input().split())
board = [input() for _ in range(M)]

cnt = []

for row in range(M - 7):
    for col in range(N - 7):
        chess = [split_board[col: col + 8] for split_board in board[row: row + 8]]
        cnt.append(check_color(chess))

print(min(cnt))