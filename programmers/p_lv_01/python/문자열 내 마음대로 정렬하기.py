# 문자열로 구성된 리스트 strings, 정수 n에서 각 문자열 인덱스 n번째 글자를 기준으로 오름차순 정렬
# 인덱스 n번째 글자가 같은 문자열일 경우 사전순으로 정렬


def solution_001(strings, n):
    # strings.sort(key=lambda x: (x[n], x))
    # print(strings)
    print(sorted(strings, key=lambda x: (x[n], x)))


def solution_002(strings, n):
    answer = []
    for sv in strings:
        answer.append(sv[n] + sv)

    print([av[1:] for av in sorted(answer)])


# run results
strings_001 = ["sun", "bed", "car"]
n_001 = 1
solution_001(strings_001, n_001)
solution_002(strings_001, n_001)

strings_002 = ["abce", "abcd", "cdx"]
n_002 = 2
solution_001(strings_002, n_002)
solution_002(strings_002, n_002)