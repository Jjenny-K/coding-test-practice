# 문자열 출력

# 단어 s의 가운데 글자 출력
# 단어 길이가 짝수일 경우 가운데 두글자 출력


def solution_001(s):
    center = len(s) // 2

    return s[center] if len(s) % 2 != 0 else s[center - 1: center + 1]


def solution_002(s):
    return s[(len(s) - 1) // 2: len(s) // 2 + 1]
    # return s[(len(s) - 1) // 2: -((len(s) - 1) // 2)]


# run result
s_001 = 'abcde'  # answer = 'c'
print(solution_001(s_001))
print(solution_002(s_001))

s_002 = 'qwer'  # answer = 'we'
print(solution_001(s_002))
print(solution_002(s_002))