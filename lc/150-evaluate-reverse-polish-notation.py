from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            token = tokens[i]
            if token == "+":
                rhs = stack.pop(-1)
                lhs = stack.pop(-1)
                stack.append(lhs + rhs)
            elif token == "-":
                rhs = stack.pop(-1)
                lhs = stack.pop(-1)
                stack.append(lhs - rhs)
            elif token == "*":
                rhs = stack.pop(-1)
                lhs = stack.pop(-1)
                stack.append(lhs * rhs)
            elif token == "/":
                rhs = stack.pop(-1)
                lhs = stack.pop(-1)
                stack.append(int(lhs / rhs))
            else:
                stack.append(int(token))
        return stack[0]