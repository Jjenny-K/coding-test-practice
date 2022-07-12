# stack

# 격자 상태의 인형판 board, 인형을 집기 위해 크레인을 작동시킨 위치가 담긴 moves
# 크레인을 모두 작동시킨 후 터트려져 사라진 인형의 개수 출력
# board는 인형판의 행들을 나타낸 2차원 배열, 크레인을 작동시키면 해당 열 최상단에 높여진 인형을 움직임


def solution_001(board, moves):
    answer = 0
    result = [0]
    board_col = [list(i) for i in zip(*board)]

    for i in moves:
        for j in range(len(board_col[i - 1])):
            if board_col[i - 1][j] != 0:
                if result[-1] == board_col[i - 1][j]:
                    answer += 2
                    result.pop()
                else:
                    result.append(board_col[i - 1][j])

                board_col[i - 1][j] = 0
                break

    print(answer)


def solution_002(board, moves):
    answer = 0
    stacklist = []

    for i in moves:
        for j in range(len(board)):
            if board[j][i - 1] != 0:
                stacklist.append(board[j][i - 1])
                board[j][i - 1] = 0

                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2
                break

    print(answer)


def solution_003(board, moves):
    answer, stacklist = 0, [0]
    cols = list(map(lambda x: list(filter(lambda y: y > 0, x)), zip(*board)))

    for m in moves:
        if len(cols[m - 1]) > 0:
            if (d := cols[m - 1].pop(0)) == (l := stacklist.pop()):
                answer += 2
            else:
                stacklist.extend([l, d])

    print(answer)


# run result
board_001 = [[0, 0, 0, 0, 0],
             [0, 0, 1, 0, 3],
             [0, 2, 5, 0, 1],
             [4, 2, 4, 4, 2],
             [3, 5, 1, 3, 1]
            ]
moves_001 = [1, 5, 3, 5, 1, 2, 1, 4]
solution_001(board_001, moves_001)
solution_002(board_001, moves_001)
solution_003(board_001, moves_001)