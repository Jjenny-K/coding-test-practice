# 문자열 변환

# JadenCase: 모든 단어의 첫 문자가 대문자이고, 그 외 알파벳은 소문자인 문자열
#            첫 문자가 알파벳이 아닐 경우에도 이어지는 알파벳은 소문자로 출력
# 문자열 s를 JadenCase로 변환해 출력
# 숫자는 단어의 첫 문자로만 나올 수 있음
# 숫자는 연속해서 나올 수 없고, 공백문자는 연속해서 나올 수 있음


def solution_001(s):
    return ' '.join([word[0].upper() + word[1:].lower() if word != '' else word for word in s.split(' ')])


def solution_002(s):
    return ' '.join([word.capitalize() for word in s.split(" ")])


# run result
s_001 = '3people unFollowed me'  # answer = '3people Unfollowed Me'
print(solution_001(s_001))
print(solution_002(s_001))

s_002 = ' A  best choice'  # answer = ' A  Best Choice'
print(solution_001(s_002))
print(solution_002(s_002))