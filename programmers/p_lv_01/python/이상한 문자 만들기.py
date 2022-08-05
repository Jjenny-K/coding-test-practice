# 문자열 파싱 # 문자열 출력

# 문자열 내 각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열 출력
# 단어별 짝,홀수 인덱스 판별

def solution_001(s):
    answer = ''
    s_list = s.split(' ')

    for val in s_list:
        for i, v in enumerate(val):
            if i % 2 == 0:
                answer += v.upper()
            else:
                answer += v.lower()
        answer += ' '

    return answer[:-1]


def solution_002(s):
    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))


# run result
s_001 = 'try hello world '  # answer = 'TrY HeLlO WoRlD '
print(solution_001(s_001))
print(solution_002(s_001))