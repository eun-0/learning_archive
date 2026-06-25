# 1. [데이터 정제] 리스트와 문자열 필터링

# 미션 1: 조건에 맞는 데이터 추출
# [ (표현식) for (항목) in (반복가능객체) if (조건문) ]
numbers = [1, 2, 3, 4, 5, 6]

even = [num  ** 2 for num in numbers if num % 2 == 0]
print(even)

numbers = [1, 3, 5]
output = [num for num in numbers if num % 2== 0]
print(output)


# 미션 2: 데이터 묶기 (Zip & Unpacking)
names= ["철수", "영희", "민수"]
scorce = [90, 85, 70]

students = dict(zip(names, scorce))
print(students)


# 2. [효율성] 집합과 해시 카운팅
# 미션 3: 중복 제거 및 교집합 찾기
listA = [1, 5 ,2, 3]
listB = [2, 3, 4, 5, 9]

inter = set(listA) & set(listB)
print(inter)


# 미션 4: 문자열 빈도수 계산기
from collections import Counter

s = "banana"

counts = Counter(s)
print(dict(counts))

s2 = "mississippi"
counts2 = Counter(s2)
print(dict(counts2))