# 브루드 포스

# 분해합: 임의의 자연수 n과 n을 이루는 각 자리수의 합
# 생성자: 임의의 자연수 m의 분해합
# 자연수 n이 주어질 때, n의 가장 작은 생성자 출력, 없을 경우 0 출력

target = int(input())

# 주어진 target에서 각 자리 수의 최대 수를 빼면 생성자인지 판단해야하는 자연수의 최솟값 도출
# 해당 값이 target보다 크다면 최솟값 0으로 지정
max_digits = len(str(target)) * 9
start_search = 0

if target > max_digits:
    start_search = target - max_digits

for n in range(start_search, target):
    sum_digits = sum(map(int, str(n)))

    if (n + sum_digits) == target:
        print(n)
        break
else:
    print(0)