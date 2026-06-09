# [기초] 변수와 연산자
# 미션1: 변수 타입과 형 변환(Type Casting)
a = 100
b = '200'

result = a + int(b)
print(f'숫자 {a} + 문자열 "{b}" -> 숫자 {result}')


#---------------------------------------------------------------------------
# 미션2: 산술 연산과 비교(Operators)
num1 = 10
num2 = 3

# 덧셈 (+)
add_result = num1 + num2

# 뺄셈 (-)
sub_result = num1 - num2

# 곱셈 (*)
mul_result = num1 * num2

# 몫 (//)
div_result = num1 // num2

results = [add_result, sub_result, mul_result, div_result]
results_bl = num1 > num2

print(f'사칙연산 : {results}')
print(f'비교 : {results_bl}')

#---------------------------------------------------------------------------
# [제어] 조건문과 반복문
# 미션3: 조건에 따른 로직 분기(If-Elif-Else)
score = 85

if score >= 90:
    grade = 'A'
elif score >= 70:
    grade = 'B'
else:
    grade = 'C'

print(f"점수: {score}, 학점: {grade}")

#---------------------------------------------------------------------------
# 미션4: 범위 반목문 활용(For Loop & Range)
n = 5
total_sum = 0

for i in range(1, n+1):
    total_sum += i
print(f'출력: {total_sum}')

#---------------------------------------------------------------------------
# [문자열&리스트] 기초 조작
# 미션5: 문자열 포맷팅과 인덱싱(String Formatting)
name = 'Alice'
age = 25
first_char = name[0]

print(f'my name is {name} and i am {age} years old, "{first_char}"')

#---------------------------------------------------------------------------
# 미션6: 리스트 다루기(List Operations)
numbers = []
new_numbers = [1, 2, 3]

for n in new_numbers:
    numbers.append(n)

list_len = len(numbers)

print(f'숫자 추가 후: {numbers}')
print(f'리스트의 길이: {list_len}')