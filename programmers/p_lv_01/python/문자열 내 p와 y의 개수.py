# 대소문자가 섞여있는 문자열 s에서 p와 y의 개수가 같으면 true, 다르면 false 출력
# p와 y가 하나도 없는 경우 true
import collections


def solution_001(s):
    return s.lower().count('p') == s.lower().count('y')


def solution_002(s):
    cnt = collections.Counter(s.lower())
    return cnt['p'] == cnt['y']


# run result
s_001 = 'PoooyY'  # answer = False
print(solution_001(s_001))
print(solution_002(s_001))

s_002 = 'aBcdEfg'  # answer = True
print(solution_001(s_002))
print(solution_002(s_002))