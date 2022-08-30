# 백트래킹

# 자연수 N, M이 주어질 때, 1부터 N까지 자연수 중 중복없이 M개를 고른 오름차순 수열 출력
# 수열은 공백으로 구분해 사전순으로 출력

import itertools

N, M = map(int, input().split())

permutation = list(itertools.combinations(range(1, N + 1), M))

for case in permutation:
    print(' '.join(str(i) for i in case))