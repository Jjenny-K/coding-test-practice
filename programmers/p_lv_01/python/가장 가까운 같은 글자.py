# 완전 탐색 # 문자열 파싱

# 문자열의 각 위치 마다 자신보다 앞에 나왔으면서, 자신과 가장 가까운 곳에 있는 같은 글자 위치 파악
# 자신보다 앞에 같은 글자가 없을 경우 -1로 표현
# 자신보다 앞에 같은 글자가 있을 경우 가장 가까운 위치 표현
# 문자열 s가 주어질 때, 각 위치마다 가장 가까운 같은 글자의 위치 출력


def solution(s):
    answer = []

    for idx, value in enumerate(s):
        close_string = s[:idx][::-1].find(value)

        if close_string != -1:
            close_string += 1

        answer.append(close_string)

    return answer


# run result
s_001 = 'foobar'  # answer = [-1, -1, 1, -1, -1, -1]
print(solution(s_001))