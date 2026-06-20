# [심화] 고급 변환 및 데이터 정제
# Map, reduce, Lambda를 활용한 일괄 변환
from functools import reduce

# map 함수
numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x: x**2, numbers)
print(list(squared_numbers))


# reduce 함수 
# 연산 누적
sum_of_numbers = reduce(lambda x,y: x + y, numbers)
print(sum_of_numbers)


# 문자열 누적 결합
words = ['Today', 'is', 'a', 'perfect', 'day', 'to', 'be', 'happy']
sentence = reduce(lambda x, y: f'{x} {y}', words)
print(f'완성된 문장: {sentence}')


# 누적 비교 연산
score_list = [75, 92, 88, 64, 95, 82]
highest_score = reduce(lambda x, y: x if x > y else y, score_list)
print(f'최고 점수: {highest_score}')


# MapReduce 패턴
orders = [('키보드', 2), ('마우스', 5), ('모니터', 3), ('거치대', 3)]
quantity_list = map(lambda order: order[1], orders)
total_quantity = reduce(lambda x, y: x + y, quantity_list)
print(f'오늘 판매된 총 상품 개수: {total_quantity}')


#-------------------------------------------------------------------------------------------
# 슬라이싱을 이용한 데이터 추출
sensor_data = [10.5, 11.2, 10.8, 12.1, 11.0, 11.9]

reversed_indices = sensor_data[::-1]
even_indices = sensor_data[::2]
odd_indices = sensor_data[1::2]

print(f'역순 인덱스 데이터: {reversed_indices}')
print(f'짝수 인덱스 데이터 : {even_indices}')
print(f'홀수 인덱스 데이터 : {odd_indices}')


#-------------------------------------------------------------------------------------------
# 정렬 메서드 비교 및 Key를 이용한 커스텀 정렬
# 원본 수정 .sort()와 새로운 리스트를 반환하는 .sorted()
sensor_data = [10.5, 11.2, 10.8, 12.1, 11.0, 11.9]
sensor_sort = sensor_data.sort()

print(f'sort() 메서드 반환한 값: {sensor_sort}')
print(f'정렬 후 원본 데이터: {sensor_data}')

sensor_data2 = [10.5, 11.2, 10.8, 12.1, 11.0, 11.9]
sensor_sorted = sorted(sensor_data2)

print(f'sorted() 전 원본: {sensor_data2}')
print(f'sorted() 후 원본: {sensor_data2}')
print(f'sorted() 결과: {sensor_sorted}')


# Key를 이용한 커스텀 정렬
words = ['apple', 'no', 'banana', 'cat']
words.sort(key=lambda x: (len(x), x))

print(f'정렬된 단어 리스트: {words}')


person_data = [('Luna', 20), ('Bella', 15), ('Mia', 17)]
sorted_by_age = sorted(person_data, key = lambda x: x[1], reverse=False)
print(f'나이 기준 정렬: {sorted_by_age}')


#-------------------------------------------------------------------------------------------
# Set 집합 연산

set_a = {1, 2, 3, 4, 5}
set_b = {3, 4, 5, 6, 7}

# 합집합(Union), (A | B)
print(f'합집합 :', set_a | set_b)

# 교집합(Intersection), (A & B)
print(f'교집합 :', set_a & set_b)

# 차집합(Difference), (A - B)
print(f'차집합 :', set_a - set_b)

# 대칭차집합(Symmetric Difference), (A ^ B)
print(f'대칭차집합 :', set_a ^ set_b)