# 정렬 # list

# 문자열 s에 나타나는 문자를 큰 것부터 작은 순으로 정렬해 출력
# 대문자는 소문자보다 작은 것으로 간주


def solution_001(s):
    return ''.join(sorted(s, reverse=True))


def solution_002(s):
    return ''.join([chr(n) for n in sorted([ord(c) for c in list(s)], reverse=True)])


# run result
s_001 = 'Zbcdefg'  # answer = 'gfedcbZ'
print(solution_001(s_001))
print(solution_002(s_001))