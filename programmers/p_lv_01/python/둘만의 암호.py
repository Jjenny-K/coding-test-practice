# 완전 탐색 # 문자열 변환

# 문자열의 각 알파벳을 일정수 뒤의 알파벳으로 바꾼 문자열 반환(임의 문자는 제외)
# 일정수 뒤의 알파벳이 z를 넘어갈 경우 다시 a로 루프
# 문자열 s, 제외 문자열 skip, 일정수 index가 주어질 때, 변환한 문자열 출력


def solution_001(s, skip, index):
    answer = ''
    alpha = list('abcdefghijklmnopqrstuvwxyz')

    # skip 문자 제거
    for rv in skip:
        alpha.remove(rv)

    # s 변환
    for value in s:
        answer += alpha[(alpha.index(value) + index) % len(alpha)]

    return answer


def solution_002(s, skip, index):
    answer = ''
    skip = set(ord(w) for w in skip)

    for word in s:
        cnt = index
        word = ord(word)

        while cnt != 0:
            word += 1

            if word > ord('z'):
                word = word - ord('z') + ord('a') - 1

            if word in skip:
                continue

            cnt -= 1

        answer += chr(word)

    return answer


# run result
s_001 = 'aukks'  # answer = 'happy'
skip_001 = 'wbqd'
index_001 = 5
print(solution_001(s_001, skip_001, index_001))
print(solution_002(s_001, skip_001, index_001))