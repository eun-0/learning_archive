# 파이썬 기초 문법 - 개념자료 


# 3. 연산자 체계와 연산 효율성(Operators)
# 3.1 산술 연산자의 정밀한 활용
total = 10
count = 3

print(f'실수 나눗셈: {total/count}')
print(f'몫 연산(//): {total//count}')
print(f'나머지 연산(%): {total%count}')

result = (total + 5) * (count **2)

def operators(num1, num2):
    return [num1+num2, num1-num2, num1*num2, num1//num2]

print(operators(10, 3))

def comparison(num1, num2):
    return num1 > num2

print(comparison(10, 3))


# 3.2 논리 연산과 단락 평가(Short-circuit Evaluation)
def check_status():
    print('시스템 상태 확인 중...')
    return True

items = []
if items and check_status():
    print('아이템이 존재하며 시스템이 정상입니다.')
else: 
    print('아이템이 없거나 확인을 생략했습니다.')
    
    
def buy(money, price):
    if money >= price:
        return '물건을 구매했습니다.'
    else:
        return '돈이 부족합니다.'

print(buy(5000,2000))


# 4. 제어문을 통한 논리 흐름의 설계(Control Flow)
# 4.1 조건문의 논리적 배타성
price = 100000

if price >= 100000:
    print('최우수 회원입니다')
elif price >= 50000:
    print('일반 회원입니다.')
else:
    print('새싹 회원입니다.')
    

# 4.2 반복문과 range 객체의 성능
total_sum = 0
for i in range(1, 101):
    total_sum += i
    
print(total_sum)


matrix = [[1, 2], [3, 4], [5, 6]]
for row in matrix:
    for element in row:
        print(element, end=" ")


# 5. 문자열 및 리스트 자료구조의 조작(Sequence Types)
# 5.1 가독성 중심의 문자열 포맷팅
name = 'Student'
rank = 1
message = f'안녕하세요. {name}님! 현재 당신의 순위는 {rank}위입니다'

print(message)

# 5.2 리스트의 동적 관리와 시간 복잡도
numbers = []
numbers.append(10)
numbers.append(20)
numbers.append(30)

last_item = numbers.pop()
current_size = len(numbers)
print(f'첫 요소: {numbers[0]}, 마지막 요소: {numbers[-1]}')