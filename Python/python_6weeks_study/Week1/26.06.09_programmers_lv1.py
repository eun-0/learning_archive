# 예제 문제 따라하기

# 1. 병렬 처리와 인덱싱의 효율화(Parallel Iteraton)
# 1.1 zip() 함수를 활용한 데이터 결합 및 매핑
subjects = ["Math", "Science", "History"]
scores = [95, 88, 92]

score_dict = dict(zip(subjects, scores))

print('---1.1 zip() 활용 결과---')
print(f'매핑된 딕셔너리: {score_dict}')


# 1.2 enumerate()를 통한 인덱스 관리의 안정성 확보
nums = [1, 2, 3, 2, 1]
target = 2

target_indices = [idx for idx, val in enumerate(nums) if val == target]

print('\n---1.2 enumerate() 활용 결과---')
print(f'타겟  "{target}"의 위치 리스트: {target_indices}')


# 2. 문자열 연산과 조건 제어 최적화(String & Optimization)
# 2.1 join()메서드와 불변 객체의 메모리 전략
words = ['Python', 'is', 'a', 'powerful', 'language']
sentence = ' '.join(words)

print('\n---2.1 join() 활용 결과---')
print(f'결합된 문장: "{sentence}"')


# 2.2 중첩 삼항 연산자(Ternary Operator)의 가독성
n = 0
status = 'Positive' if n > 0 else ('Zero' if n == 0 else 'Negative')

print('\n---2.2 삼항 연산자 결과---')
print(f'숫자 {n}의 상태 판별: {status}')


# 3. 데이터 언패킹과 효울적인 멤버십 테스트(Unpacking & Sets)
# 3.1 가변 언패킹(*)을 이용한 데이터 분리
scores = [50, 70, 80, 90, 100]
min_val, *mid_vals, max_val = scores

print('\n---3.1 가변 언패킹 결과---')
print(f'최소: {min_val}, 최대: {max_val}, 분석 대상: {mid_vals}')


# 3.2 in 연산자와 집합(Set)의 해시 메커니즘
vowels = {'a', 'e', 'i', 'o', 'u'}
target_word = 'apple'

contains_vowel = any(char in vowels for char in target_word)

print('\n---3.2 멤버십 테스트 결과---')
print(f"'{target_word}'에 모음 포함 여부: {contains_vowel}")


# 4. 함수형 프로그래밍과 커스텀 정렬(Function Approach)
# 4.1 map()과 lambda를 통한 일괄 변환
str_nums = ['1', '2', '3']
int_nums = list(map(int, str_nums))

print('\n---4.1 map/lambda 결과---')
print(f'변환된 정수 리스트: {int_nums}')


# 4.2 슬라이싱의 Step 인자를 활용한 데이터 정제
s = 'abcdef'
even_indexed_chars = s[::2]

print('\n---4.2 슬라이싱 Step 결과---')
print(f'짝수 인덱스 문자열: {even_indexed_chars}')


# 4.3 key 인자와 lambda를 이용한 다중 기준 정렬
words = ['apple', 'no', 'banana', 'cat']

words.sort(key=lambda x: (len(x), x))

print('\n---4.3 커스텀 정렬 결과---')
print(f'정렬된 단어 리스트: {words}')


# 5. 집합 연산을 통한 데이터 비교 및 정제(Set Operations)
list_a = [1, 2, 2, 3]
list_b = [3, 4]

unique_to_a = list(set(list_a) - set(list_b))

print('\n---5. 집합 연산 결과---')
print(f'A에만 존재하는 원소(중복 제거): {unique_to_a}')

#---------------------------------------------------------------------------
# 파이썬스러운 코드(Pythonic Code) 작성 미션

# 1. [병렬 처리와 인덱스] 효율적인 루프 구성
# 미션1: Zip을 활용한 데이터 매핑
subjects = ['Math', 'Sci']
scores = [90, 800]

subject_score_dict = dict(zip(subjects, scores))
print(f'매핑된 딕셔너리: {subject_score_dict}')


# 미션2: Enumerate를 활용한 조건부 인덱스 찾기
nums = [1, 2, 3, 2, 1]
target = 2

target_index = [idx for idx, val in enumerate(nums) if val == target]

print(f'타겟 "{target}"의 위치 리스트: {target_indices}')


# 2. [문자열 및 조건] 성능과 가독성 최적화
# 미션3: Join을 활용한 문자열 결합
words = ['Python', 'is', 'Easy']
sentence = ' '.join(words)

print(f'결합된 문장: {sentence}')


# 미션4: Ternary Operator를 이용한 인라인 조건문
n = -5
status = 'Positive' if n > 0 else 'Negative'

print(f'숫자 {n}의 상태 판별: {status}')


# 3. [데이터 구조화] 언패킹과 멤버십 테스트
# 미션5: 별표(*)를 활용한 가변 언패킹
data = [50, 70, 80, 90, 100]
min_data, *mid_data, max_data = data

print(f'min={min_data}, mid={mid_data}, max={max_data}')


# 미션6: In 연산자를 활용한 존재 여부 확인
vowels = {'a', ' e', 'i', 'o', 'u'}

def contains_vowel(word):
    return any(char in vowels for char in word)

print(f'"sky"에 모음 포함 여부: {contains_vowel(word="sky")}')
print(f'"apple"에 모음 포함 여부: {contains_vowel(word="apple")}')


# 4. [심화] 고급 변환 및 데이터 정제
# 미션7: Map과 Lambda를 활용한 일괄 변환
str_nums = ['1', '2', '3']
int_nums = list(map(lambda x: int(x), str_nums))

print(f'변환된 정수 리스트: {int_nums}')


# 미션8: 슬라이싱 Step을 이용한 데이터 추출
s = 'abcdef'
indexs_step = s[::2]

print(f'짝수 인덱스 문자열: {indexs_step}')


# 미션9: Key를 이용한 커스텀 정렬 (문자열 길이)
words = ['apple', 'no', 'banana', 'cat']
words.sort(key=lambda x: (len(x), x))

print(f'정렬된 단어 리스트: {words}')


# 미션10: Set 차집합을 이용한 유일 원소 찾기
A = [1, 2, 2, 3]
B = [3, 4]
result = list(set(A) - set(B))

print(f'A에만 존재하는 원소: {result}')