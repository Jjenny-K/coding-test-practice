# 문자열 s 길이가 4, 6이고 숫자로만 구성되어 있는지 확인해 출력
import re


def solution_001(s):
    # print(True if len(s) in [4, 6] and s.isdigit() else False)
    print(len(s) in (4, 6) and s.isdigit())


def solution_002(s):
    try:
        int(s)
        print(len(s) in (4, 6))
    except:
        print(False)


def solution_003(s):
    print(bool(re.match("^(\d{4}|\d{6})$", s)))


# run result
s_001 = 'a234'
solution_001(s_001)
solution_002(s_001)
solution_003(s_001)