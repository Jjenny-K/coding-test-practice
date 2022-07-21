# 완전탐색 # 경우의 수 # max & min

# 명함의 가로, 세로 길이를 나타내는 2차원 배열 sizes에서 모든 명함을 수납할 수 있는 가장 작은 지갑의 크기 출력
# 명함을 가로로 눞혀서 수납할수도 있음


def solution_001(sizes):
    min_list = []
    max_list = []

    for i, j in sizes:
        min_list.append(min(i, j))
        max_list.append(max(i, j))

    return max(min_list) * max(max_list)
    # return max(max(x) for x in sizes) * max(min(x) for x in sizes)


def solution_002(sizes):
    return max(sum(sizes, [])) * max(min(size) for size in sizes)


# run result
sizes_001 = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]  # answer = 133
print(solution_001(sizes_001))
print(solution_002(sizes_001))