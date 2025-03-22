# https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+', '-', '*', '/'}
        for token in tokens:
            if token in operators:
                b, a = stack.pop(), stack.pop()
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                else:
                    stack.append((abs(a) // abs(b)) * (-1 if b < 0 else 1) * (-1 if a < 0 else 1))
            else:
                stack.append(int(token))
        return stack[-1]

        
