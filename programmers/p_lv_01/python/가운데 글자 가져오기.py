# 단어 s의 가운데 글자 출력
# 단어 길이가 짝수일 경우 가운데 두글자 출력


def solution_001(s):
    center = len(s) // 2

    print(s[center] if len(s) % 2 != 0 else s[center - 1: center + 1])


def solution_002(s):
    print(s[(len(s) - 1) // 2: len(s) // 2 + 1])
    # print(s[(len(s) - 1) // 2: -((len(s) - 1) // 2)])


# run result
s_001 = 'abcde'
solution_001(s_001)
solution_002(s_001)

s_002 = 'qwer'
solution_001(s_002)
solution_002(s_002)