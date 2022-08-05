# 문자열 파싱

# 다트 게임 점수를 계산해 출력
# 기회: 총 3번, 점수: 0 - 10 범위
# S: 점수^1, D: 점수^2, T: 점수^3, *: 점수*2(*, #과 중첩가능 -> 점수*4, 점수*-2), #: 점수*-1
import re


def solution_001(dart_result):
    answer = []
    n = ''

    for val in dart_result:
        if val.isnumeric():
            n += val
        elif val == 'S':
            n = int(n) ** 1
            answer.append(n)
            n = ''
        elif val == 'D':
            n = int(n) ** 2
            answer.append(n)
            n = ''
        elif val == 'T':
            n = int(n) ** 3
            answer.append(n)
            n = ''
        elif val == '*':
            if len(answer) > 1:
                answer[-2] = answer[-2] * 2
                answer[-1] = answer[-1] * 2
            else:
                answer[-1] = answer[-1] * 2
        elif val == '#':
            answer[-1] = answer[-1] * -1

    return sum(answer)


def solution_002(dart_result):
    answer = []

    dart_result = dart_result.replace('10', 'k')
    point = ['10' if i == 'k' else i for i in dart_result]

    i = -1
    sdt = {'S': 1, 'D': 2, 'T': 3}
    for j in point:
        if j in sdt.keys():
            answer[i] = answer[i] ** sdt[j]
        elif j == '*':
            answer[i] = answer[i] * 2
            if len(answer) > 1:
                answer[i - 1] = answer[i - 1] * 2
        elif j == '#':
            answer[i] = answer[i] * (-1)
        else:
            answer.append(int(j))
            i += 1

    return sum(answer)


def solution_003(dart_result):
    bonus = {'S': 1, 'D': 2, 'T': 3}
    option = {'': 1, '*': 2, '#': -1}
    p = re.compile('(\d+)([SDT])([*#]?)')

    dart = p.findall(dart_result)

    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i - 1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    return sum(dart)


# run result
dart_result_001 = '1D2S#10S'  # answer = 1**2 + 2**1 * (-1) + 10**1 = 9
print(solution_001(dart_result_001))
print(solution_002(dart_result_001))
print(solution_003(dart_result_001))

dart_result_002 = '1S*2T*3S'  #	answer = 1**1 * 2 * 2 + 2**3 * 2 + 3**1 = 23
print(solution_001(dart_result_002))
print(solution_002(dart_result_002))
print(solution_003(dart_result_002))

dart_result_003 = '1D#2S*3S'  # answer = 1**2 * (-1) * 2 + 2**1 * 2 + 3**1 = 5
print(solution_001(dart_result_003))
print(solution_002(dart_result_003))
print(solution_003(dart_result_003))