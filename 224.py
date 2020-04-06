class Solution:
    def calculate(self, s: str) -> int:
        num = 0
        result = 0
        sign = 1
        stack = [1]
        for i in s+'+':
            if i.isdigit():
                num = num*10 + int(i)
            elif i == '+':
                result += num*sign*stack[-1]
                num = 0
                sign = 1
            elif i == '-':
                result += num*sign*stack[-1]
                num = 0
                sign = -1
            elif i == '(':
                stack.append(sign*stack[-1])
                sign = 1
            elif i == ')':
                result += num*sign*stack[-1]
                num = 0
                stack.pop()
        return result
