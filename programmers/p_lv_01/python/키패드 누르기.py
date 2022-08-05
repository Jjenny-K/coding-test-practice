# 탐색 # 맨해튼 거리 # DFS, BFS...?

# 전화 키패드에서 왼손과 오른손의 엄지손가락만 이용해서 숫자를 입력할 때 사용되는 손 위치 출력
# 초기 왼손 엄지손가락 '*', 오른손 엄지손가락 '#'
# 상하좌우 4가지 방향으로만 이동, 키패드 이동 한 칸 == 거리 1 이동
# 1, 4, 7 입력시 왼손 엄지손가락, 3, 6, 9 입력시 오른손 엄지손가락 사용
# 2, 5, 8, 0 입력시 두 엄지손가락 현재 위치에서 더 가까운 엄지손가락 사용, 같을 경우 hand 사용


def solution(numbers, hand):
    answer = ''
    keypad = {1: [0, 0], 2: [0, 1], 3: [0, 2],
              4: [1, 0], 5: [1, 1], 6: [1, 2],
              7: [2, 0], 8: [2, 1], 9: [2, 2],
              '*': [3, 0], 0: [3, 1], '#': [3, 2]}
    left, right = '*', '#'

    for number in numbers:
        if number in [1, 4, 7, '*']:
            answer += 'L'
        elif number in [3, 6, 9, '#']:
            answer += 'R'
        else:
            nx, ny = keypad[number]
            lx, ly = keypad[left]
            rx, ry = keypad[right]

            abs_left = (abs(nx - lx) + abs(ny - ly))
            abs_right = (abs(nx - rx) + abs(ny - ry))
            if abs_left > abs_right:
                answer += 'R'
            elif abs_left < abs_right:
                answer += 'L'
            else:
                answer += hand.upper()[0]

        if answer[-1] == 'L':
            left = number
        else:
            right = number

    return answer


# run result
numbers_001 = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]  # answer = 'LRLLRRLLLRR'
hand_001 = 'left'
print(solution(numbers_001, hand_001))