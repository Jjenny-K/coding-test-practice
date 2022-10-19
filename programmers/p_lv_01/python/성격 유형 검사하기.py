# 문자열 파싱 및 출력

# 성격 유형 검사 지표, 선택지 점수가 주어질 때, 검사자의 성격 유형 검사 결과 지표 순서대로 출력
"""
성격 유형 검사 지표
1. 라이언형(R), 튜브형(T)
2. 콘형(C), 프로도형(F)
3. 제이지형(J), 무지형(M)
4. 어피치형(A), 네오형(N)

선택지 점수
1. 매우 비동의 (3점)
2. 비동의 (2점)
3. 약간 비동의 (1점)
4. 모르겠음 (0점)
5. 약간 동의 (1점)
6. 동의 (2점)
7. 매우 동의 (3점)
"""
# 각 질문의 판단 지표에서 첫번째 요소는 비동의 관련 선택지를 선택할 경우, 두번째 요소는 동의 관련 선택지를 선택할 경우 받는 성격 유형
# 각 성격 유형 검사 지표에서 점수를 높게 받은 유형이 선택되며, 같은 점수를 받을 경우 사전 순으로 빠른 유형을 선택


def solution(survey, choices):
    # 선택별 점수, 검사 결과 초기화
    score = {1: 3, 2: 2, 3: 1, 4: 0, 5: 1, 6: 2, 7: 3}
    result = {'R': 0, 'T': 0, 'C': 0, 'F': 0,
              'J': 0, 'M': 0, 'A': 0, 'N': 0}

    for s, c in zip(survey, choices):
        if c <= 3:
            # 비동의 관련 선택지를 선택한 경우
            result[s[0]] += score[c]
        elif c >= 5:
            # 동의 관련 선택지를 선택한 경우
            result[s[1]] += score[c]

    answer = ''

    answer += 'R' if result['R'] >= result['T'] else 'T'
    answer += 'C' if result['C'] >= result['F'] else 'F'
    answer += 'J' if result['J'] >= result['M'] else 'M'
    answer += 'A' if result['A'] >= result['N'] else 'N'

    return answer


# run result
survey_001 = ["AN", "CF", "MJ", "RT", "NA"]  # answer = 'TCMA'
choices_001 = [5, 3, 2, 7, 5]
print(solution(survey_001, choices_001))

survey_002 = ["TR", "RT", "TR"]  # answer = 'RCJA'
choices_002 = [7, 1, 3]
print(solution(survey_002, choices_002))