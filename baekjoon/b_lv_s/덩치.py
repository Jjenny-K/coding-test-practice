# 브루트 포스

# 사람의 덩치를 키, 몸무게 값으로 표현해 등수 지정
# 몸무게 x kg, 키 y cm인 사람의 덩치는 (x, y)로 표현
# A, B 두 사람의 덩치 (x, y), (p, q)에서 x > p, y > q일 경우 A가 B보다 덩치가 크다 할 수 있음
# n명 집단에서 각 사람의 덩치 등수를 자신보다 더 큰 덩치의 사람 수 + 1이라 할 때, 각 사람의 덩치 등수를 공백으로 분리해 출력

people = int(input())
sizes = [tuple(map(int, input().split())) for _ in range(people)]

answer = []

for x, y in sizes:
    cnt = 0

    for p, q in sizes:
        if x < p and y < q:
            cnt += 1

    answer.append(str(cnt + 1))

print(' '.join(answer))