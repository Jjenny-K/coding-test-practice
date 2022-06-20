# 0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수
# 배열 numbers 원소 순서를 재배치하여 만들 수 있는 가장 큰 수 출력
# 0 <= numbers 원소 <= 1000

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)
    print(str(int(''.join(numbers))))


# run result
numbers_001 = [3, 30, 34, 5, 9]
solution(numbers_001)