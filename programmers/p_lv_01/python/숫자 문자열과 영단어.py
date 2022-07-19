# 문자열 변환

# 일부 자릿수를 영단어로 바꾼 숫자에서 원래 숫자 출력
# 각 숫자는 영어 영단어와 대응


def solution_001(s):
    words = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
             '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}

    for k, v in words.items():
        s = s.replace(v, k)

    return int(s)


def solution_002(s):
    words = ['zero', 'one', 'two', 'three', 'four',
             'five', 'six', 'seven', 'eight', 'nine']

    for i, v in enumerate(words):
        s = s.replace(v, str(i))

    return int(s)


# run result
s_001 = '2three45sixseven'  # answer = 234567
print(solution_001(s_001))
print(solution_002(s_001))