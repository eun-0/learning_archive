# 스택(Stack): 후입선출(LIFO)

#---------------------------------------------
# 1. 스택의 개념과 추상 데이터 타입(ADT)
#---------------------------------------------

# 스택은 "쌓아 올린 더미"를 의미, 가장 마지막 삽입된 데이터가 가장 먼저 제거되는 후입선출 원칙을 따름. 
# 이는 컴퓨터 과학에서 함수의 실행 흐름을 관리하는 "콜 스택"의 핵심 원리이기도 함

# Push: 테이터를 스택의 가장 상단에 추가하는 연산
# Pop: 가장 상단에 위치한 데이터를 제거하고 그 값을 반환하는 연산


#---------------------------------------------
# 2. 문자열 뒤집기와 역순 처리
#---------------------------------------------
def reverse_string_with_stack(my_string):
    stack = []
    
    # 문자열의 각 문자를 스펙에 순차적으로 삽입(Push)
    for char in my_string:
        stack.append(char)
        
    reversed_str = ""
    
    # 스텍이 빌 때까지 요소를 하나씩 추출(Pop)
    while stack:
        reversed_str += stack.pop()
        
    return reversed_str

print(reverse_string_with_stack("Hello World"))



#---------------------------------------------
# 2.1 list를 이용한 스택
#---------------------------------------------
stack = []
print(f"초기 스택: {stack}")

# PUSH 연산: 데이터 추가
stack.append(10)
stack.append(20)
stack.append(30)
print(f"데이터 PUSH후: {stack}")

# PEEK 연산: 데이터 엿보기
if stack:
    popped_element = stack[-1]
    print(f"스택 최상단 데이터: {popped_element}")
    print(f"현재 스택 상태(데이터 유지): {stack}")
    
# POP 연산: 최상단 데이터 추출 및 제거
popped_element = stack.pop()
print(f"POP된 데이터: {popped_element}, 스택 상태: {stack}")


#---------------------------------------------
# 3. 괄호 유효성 검사(Syntax Analysis)
#---------------------------------------------
def is_valid_parentheses(s):
    stack = []
    # 닫는 괄호를 key, 여는 괄호를 value에 맵핑
    mapping = {")": "(", "}": "{", "]": "["}
    
    for char in s:
        if char in mapping.values():
            # 여는 괄호를 만나면 스택에 저장
            stack.append(char)
            
        elif char in mapping.keys():
            # 닫는 괄호를 만났을 때 스택이 비어있다면 짝이 맞지 않는 상황임
            if not stack or mapping[char] != stack.pop():
                return False
        
        else: 
            # 괄호 아닌 다른 문자는 무시
            continue   
        
    # 루프 종료 후 스택이 비어있어야 모든 짝이 맞은 것
    return not stack

test_cases = [
    "()",
    "()[]{}",
    "(]",
    "([)]",
    "{[]}",
    "[[",
    "var a = {b: [1, 2]};" 
]

for case in test_cases:
    if is_valid_parentheses(case):
        print(f"{case} → 유효함")
    else:
        print(f"{case} → 유효하지 않음")