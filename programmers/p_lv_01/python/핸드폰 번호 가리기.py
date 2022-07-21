# 문자열 변환

# 전화번호 문자열 phone_number에서 뒷자리 4자리를 제외한 나머지 숫자를 '*'로 가린 문자열 출력
import re


def solution_001(phone_number):
    return "*" * len(phone_number[0:-4]) + phone_number[-4:]


def solution_002(phone_number):
    pn = re.compile(r'\d(?=\d{4})')

    return pn.sub('*', phone_number, count=0)


# run result
phone_number_001 = '01033334444'  # answer = '*******4444'
print(solution_001(phone_number_001))
print(solution_002(phone_number_001))