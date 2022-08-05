# 수학 # 하노이의 탑 # 동적계획법

# 하노이의 탑: 세 개의 기둥 중 한 기둥에 작은 것이 위에 있도록 원판이 순서대로 쌓여있고, 마지막 기둥에 그 순서 그대로 옮겨 다시 쌓는 것
# 한번에 하나의 원판만 옯길 수 있고, 큰 원판이 작은 원판 위에 있어서는 안됨
# 초기 기둥에 n개의 원판이 주어질 때, 마지막 기둥으로 최소로 옮기는 방법 출력

def solution(n):
    def _hanoi(n, start, end, assis):
        answer = []

        if n == 1:
            return [[start, end]]

        answer.extend(_hanoi(n - 1, start, assis, end))
        answer.extend([[start, end]])
        answer.extend(_hanoi(n - 1, assis, end, start))

        return answer

        # return _hanoi(n - 1, start, assis, end) + [[start, end]] + _hanoi(n - 1, assis, end, start)

    return _hanoi(n, 1, 3, 2)


# run result
n_001 = 2  # answer = [[1,2], [1,3], [2,3]]
print(solution(n_001))