# 문자열 파싱

# 발음 배열 babbling이 주어질 때, 발음할 수 있는 단어의 개수 출력
# 주어진 발음을 조합해서 만들 수 있는 발음만 가능
# 연속해서 같은 발음 불가능


def solution(babbling):
    pronunciation = ['aya', 'ye', 'woo', 'ma']
    answer = 0

    for b in babbling:
        for p in pronunciation:
            if p * 2 not in b:
                b = b.replace(p, ' ')

        if b.isspace():
            answer += 1

    return answer


# run result
babbling_001 = ["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]  # answer = 2
print(solution(babbling_001))