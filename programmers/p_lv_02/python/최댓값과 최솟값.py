# 문자열 파싱 # max & min

# 공백으로 구분된 숫자들이 저장되어 있는 문자열 s에서 최소값과 최대값을 찾아 '최소값 최대값' 형태로 출력

def solution_001(s):
    s_num = list(map(int, s.split(' ')))

    # return ' '.join(map(str, [min(s_num), max(s_num)]))
    # return str(min(s_num)) + " " + str(max(s_num))
    return f'{min(s_num)} {max(s_num)}'


def solution_002(s):
    s_num = sorted(list(map(int, s.split(' '))))

    return f'{s_num[0]} {s_num[-1]}'


# run result
s_001 = '-1 -2 -3 -4'  # answer = '-4 -1'
print(solution_001(s_001))
print(solution_002(s_001))