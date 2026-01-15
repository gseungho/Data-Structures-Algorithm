# 입력: 중위 표기로 된 수식 문자열(+,-,*,(,), 숫자로만 구성, 예: "3 + 5 * (2 - 8)")
# 출력: 후위 표기로 된 수식 문자열(예: "3 5 2 8 - * +") 및 계산 결과

'''
1. 중위(infix) 표기 수식을 후위(postfix) 표기 수식으로 변환
    1) 연산자 우선순위 정의
    2) 중위 표기 수식 순회
    3) 피연산자(숫자)는 바로 출력
    4) 연산자는 스택에 넣되, 넣는 연산자보다 우선순위가 높거나 같은 연산자가 스택에 있으면 스택에서 꺼내 출력
    5) 왼쪽 괄호는 스택에 무조건 넣기
    6) 오른쪽 괄호가 나오면 왼쪽 괄호가 나올 때까지 스택에서 꺼내 출력
    7) 수식 끝나면 스택에 남은 연산자 모두 출력
2. 후위 표기 수식을 계산
    1) 후위 표기 수식 순회
    2) 피연산자(숫자)는 스택에 넣기
    3) 연산자가 나오면 스택에서 두 개의 피연산자를 꺼내 연산 후 결과를 스택에 넣기
    4) 수식 끝나면 스택에 남은 피연산자(숫자) 출력
'''

from basic_stack import Stack

def infix_to_postfix(expression):
    precedence = {'*': 2, '+':1, '-':1, '(':0}
    stack = Stack()
    output = []
    tokens = expression.split()
    for token in tokens:
        if token.isdigit():
            output.append(token)
        elif token == '(':
            stack.push(token)
        elif token == ')':
            while len(stack) > 0 and stack.top() != '(':
                output.append(stack.pop())
            stack.pop()  # 왼쪽 괄호 제거
        else:
            while len(stack) > 0 and precedence[stack.top()] >= precedence[token]:
                output.append(stack.pop())
            stack.push(token)
    while len(stack) > 0:
        output.append(stack.pop())
    
    return ' '.join(output)

def evaluate_postfix(postfix_expression):
    stack = Stack()
    tokens = postfix_expression.split()
    for token in tokens:
        if token.isdigit():
            stack.push(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.push(a + b)
            elif token == '-':
                stack.push(a - b)
            elif token == '*':
                stack.push(a * b)

    return stack.pop()

# 테스트
infix_expr = "3 + 5 * ( 2 - 8 )"
postfix_expr = infix_to_postfix(infix_expr)
print("Postfix Expression:", postfix_expr)  # Output: "3 5 2 8 - * +"
result = evaluate_postfix(postfix_expr)
print("Evaluation Result:", result)  # Output: -27