# 입력: 왼쪽, 오른쪽 괄호의 문자열
# 출력: 괄호가 올바르게 짝지어졌으면 True, 아니면 False

from basic_stack import Stack
def is_balanced_parentheses(s):
    stack = Stack()

    for char in s:
        if char == '(':
            stack.push(char)
        elif char == ')':
            if len(stack) == 0:
                return False
            stack.pop()

    return len(stack) == 0

# 테스트
print(is_balanced_parentheses("((()))"))  # Output: True
print(is_balanced_parentheses("(()"))     # Output: False
print(is_balanced_parentheses("(49+5)/7)"))     # Output: False