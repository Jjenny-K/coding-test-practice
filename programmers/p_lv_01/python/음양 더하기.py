# 정수의 절댓값 배열 absolutes, 정수 부호 배열 signs가 있을 때 실제 정수들의 합 출력
# signs[i]가 참일 경우 absolutes[i]의 실제 정수는 양수, 그렇지 않으면 음수를 의미


def solution_001(absolutes, signs):
    answer = 0

    for absolute, sign in zip(absolutes, signs):
        if sign:
            answer += absolute
        else:
            answer -= absolute

    print(answer)


def solution_002(absolutes, signs):
    print(sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs)))


# run result
absolutes_001 = [4, 7, 12]
signs_001 = [True, False, True]
solution_001(absolutes_001, signs_001)
solution_002(absolutes_001, signs_001)