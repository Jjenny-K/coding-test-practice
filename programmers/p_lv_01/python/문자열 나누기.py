# 완전 탐색 # 문자열 파싱

# 문자열을 왼쪽에서 오른쪽으로 읽으면서 첫번째 글자와 같은 글자, 다른 글자의 횟수가 같을 때 문자열 분리
# 남은 문자열에 대해 과정을 반복하고 남은 부분이 없을 경우 종료
# 남은 문자열에 대해 과정을 반복하고 횟수가 다른 상태에서 읽을 글자가 없다면 그 상태에서 문자열을 분리하고 종료
# 문자열 s가 주어질 때, 분해한 문자열의 개수 출력


def solution_001(s):
    answer = 0

    fs = s[0]
    fs_cnt, nfs_cnt = 0, 0

    for value in s:
        if fs_cnt == nfs_cnt:
            answer += 1
            fs = value
            fs_cnt, nfs_cnt = 0, 0

        if value == fs:
            fs_cnt += 1
        else:
            nfs_cnt += 1

    return answer


def solution_002(s):
    si = 0
    cnt = 0
    answer = 0

    for idx, value in enumerate(s):
        cnt += 1 if s[si] == value else -1

        if cnt == 0:
            answer += 1
            si = idx + 1

    return answer + 1 if cnt else answer


# run result
s_001 = 'aaabbaccccabba'  # answer = 3
print(solution_001(s_001))
print(solution_002(s_001))