# 수학 # 연산 # min # sum

# 길이가 같은 두 배열의 수를 각각 하나씩 뽑아 곱해서 누적해 더했을 때 최솟값 출력

def solution_001(A, B):
    # return sum([i * j for i, j in zip(sorted(A), reversed(sorted(B)))])
    return sum([i * j for i, j in zip(sorted(A), sorted(B, reverse=True))])


def solution_002(A, B):
    return sum(A.pop(A.index(min(A))) * B.pop(B.index(max(B))) for i in range(len(A)))


# run result
A_001 = [1, 4, 2]  # answer = 29
B_001 = [5, 4, 4]
print(solution_001(A_001, B_001))
print(solution_002(A_001, B_001))