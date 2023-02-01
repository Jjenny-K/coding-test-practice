# 완전 탐색 # 문자열 파싱

# 숫자로 이루어진 문자열 t, p가 주이질 때, t에서 p와 길이가 같은 부분문자열 중 p보다 작거나 같은 수가 나오는 횟수 출력


def solution(t, p):
    answer = 0
    length = len(p)

    for idx, value in enumerate(t):
        part_string = t[idx: idx + length]

        if len(part_string) != length:
            break

        if int(p) >= int(part_string):
            answer += 1

    return answer


# run result
t_001 = '3141592'  # answer = 2
p_001 = '271'
print(solution(t_001, p_001))