# 문자열 변환

# 시저 암호: 어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호
# 문자열 s, 거리 n에서 s를 n만큼 민 암호문 출력
import string


def solution_001(s, n):
    answer = ''
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase

    for val in list(s):
        if val.isupper():
            s_index = upper.index(val) + n
            answer += upper[s_index % 26]
        elif val.islower():
            s_index = lower.index(val) + n
            answer += lower[s_index % 26]
        else:
            answer += ' '

    return answer


def solution_002(s, n):
    answer = ''

    for val in list(s):
        if val.isupper():
            answer += chr((ord(val) - ord('A') + n) % 26 + ord('A'))
        elif val.islower():
            answer += chr((ord(val) - ord('a') + n) % 26 + ord('a'))
        else:
            answer += ' '

    return answer


# run result
s_001 = 'a B z'  # answer = 'd E c'
n_001 = 3
print(solution_001(s_001, n_001))
print(solution_002(s_001, n_001))