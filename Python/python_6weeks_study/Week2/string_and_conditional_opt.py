# [문자열 및 조건] 성능과 가독성 최적화
# Join, split을 활용한 문자열 결합


# 문장 결합
words_1 = ['Today', 'is', 'a', 'perfect', 'day', 'to', 'be', 'happy']
sentence_1 = ' '.join(words_1)
print(f'오늘의 영어 문장 : {sentence_1}')


# 문장을 단어로 변환
sentence_2 = 'Life is too short'
words_2 = sentence_2.split()
print(f'split 결과: {words_2}')


# 숫자 데이터 결합
numbers = [2026, 6, 18]
date_str = '.'.join(map(str, numbers))
print(f'변환된 날짜: {date_str}')


# 줄바꿈기준 문장 변환
texts = '''사과
딸기
바나나
체리'''

fruits_list = texts.split('\n')
fruits = ', '.join(fruits_list)

print(f'분리된 리스트: {fruits_list}')
print(f'과일 : {fruits}')


# 조건에 맞는 데이터만 결합
raw_words = ['Today', 'is', 'a', 'perfect', 'day', 'to', 'be', 'happy']
sentence_3 = ' '.join(word.upper() for word in raw_words if len(word) >= 3)
print(f'조건에 맞는 데이터: {sentence_3}')


# 필요 문장만 추출하기
email = 'python@amazing.code'

parts = email.split('@', maxsplit=1)
print(f'아이디: {parts[0]}')
print(f'도메인 영역: {parts[1]}')


#-------------------------------------------------------------------------------------------
# Ternary Operator를 이용한 인라인 조건문
# 삼항 연산자
num = 7
result = '짝수' if num % 2 == 0 else '홀수'
print(f'숫자 {num}은(는) {result}입니다.')


score = 80
messages = '합격' if score >= 80 else '불합격'
print(f'점수 {score}점은 {messages}입니다')


# 삼항 연산자 중첩
score = 85
grade = 'A' if score >= 90 else ('B' if score >= 80 else 'C')
print(f'점수: {score}점, 학점: {grade}등급')


# 조건에 따라 값 변환하기
raw_nums = [10, -2, 30, 0, -4, 3, 20]
nums = [x if x > 0 else 5 for x in raw_nums]

print(f'정제된 데이터: {nums}')


# 안전하게 데이터 값 가져오기
user = {'name': 'Alice', 'role': 'Admin'}
age = user['age'] if 'age' in user else '정보 없음'

print(f'나이 정보: {age}')


def get_max(a, b):
    return a if a > b else b

print(f'10과 20 중 큰 수: {get_max(10, 20)}')
print(f'30과 50 중 큰 수: {get_max(30, 50)}')