# 2016년 1월 1일은 금요일일때, 2016년 a월 b일은 무슨 요일인지 출력
# 요일: SUN, MON, TUE, WED, THU, FRI, SAT
from datetime import date


def solution_001(a, b):
    answer = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

    print(answer[date(2016, a, b).weekday()])


def solution_002(a, b):
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    print(days[(sum(months[:a - 1]) + b) % 7])


# run result
a_001 = 1
b_001 = 1
solution_001(a_001, b_001)
solution_002(a_001, b_001)