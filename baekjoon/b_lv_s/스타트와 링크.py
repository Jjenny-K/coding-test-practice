# 브루트 포스 # 백트래킹

# 짝수의 인원 N명을 스타트팀, 링크팀으로 분리
# N x N 형태로 이루어진 각 인원이 같은 팀에 속할 때 팀에 더해지는 능력치
# 팀에 속한 모든 쌍의 능력치의 합이 팀 능력치일 때, 두 팀의 능력치 차이의 최소 값 출력

import sys

N = int(sys.stdin.readline())
ability_level = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

visited = [False for _ in range(N)]
min_gab = 2147000000


def make_team(member, cnt):
    global min_gab

    if member == (N // 2):
        # 팀이 모두 구성되었을 경우, 팀 능력치 계산 후 능력치 차이 최소값 반환
        start_ability, link_ability = 0, 0

        for i in range(N - 1):
            for j in range(i + 1, N):
                if visited[i] and visited[j]:
                    start_ability += ability_level[i][j] + ability_level[j][i]
                elif not visited[i] and not visited[j]:
                    link_ability += ability_level[i][j] + ability_level[j][i]

        min_gab = min(abs(start_ability - link_ability), min_gab)

        if min_gab == 0:
            # 최소값이 0일 경우 리턴 후 종료
            print(min_gab)
            exit(0)

        return

    for i in range(cnt, N):
        if not visited[i]:
            visited[i] = True  # 해당 팀원을 하나의 팀으로 배정(방문하지 않았다면 방문, False -> True)
            make_team(member + 1, i + 1)
            visited[i] = False  # 다른 경우의 수를 위한 원복


make_team(0, 0)
print(min_gab)