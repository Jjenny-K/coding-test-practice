# 문자열 # 정렬

# 두 수의 임의의 자리에서 공통으로 나타느는 정수(0-9)들을 이용해 만들 수 있는 가장 큰 정수 출력
# 공통으로 나타나는 정수 중 서로 짝지을 수 있는 숫자만 사용
# 짝꿍이 존재하지 않으면 -1, 0으로만 구성되어 있다면 0
import collections


def solution_001(X, Y):
    # Counter 사용해 X, Y 각 정수 개수 파악
    x_counter = collections.Counter(X)
    y_counter = collections.Counter(Y)

    # X, Y 중복 정수 파악
    partner_numbers = sorted(list(set(X) & set(Y)), reverse=True)

    answer = ''

    if len(partner_numbers) == 0:
        # 중복된 정수가 없다면
        answer = '-1'
    elif len(partner_numbers) == partner_numbers.count('0'):
        # 중복된 정수가 '0' 뿐이라면
        answer = '0'
    else:
        # 중복된 정수가 있다면 각 정수별 데이터 개수 최소값만큼 answer에 추가
        for value in partner_numbers:
            answer += value * min(x_counter[value], y_counter[value])

    return answer


def solution_002(X, Y):
    answer = ''

    for i in range(9, -1, -1):
        answer += (str(i) * min(X.count(str(i)), Y.count(str(i))))

    if answer == '':
        return '-1'
    elif len(answer) == answer.count('0'):
        return '0'
    else:
        return answer


# run result
X_001 = '100'  # answer = '-1'
Y_001 = '2345'
print(solution_001(X_001, Y_001))
print(solution_002(X_001, Y_001))

X_002 = '100'  # answer = '0'
Y_002 = '203045'
print(solution_001(X_002, Y_002))
print(solution_002(X_002, Y_002))