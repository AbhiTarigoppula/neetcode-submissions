class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        total = 0

        for token in tokens:
            if token == '+':
                total = stack.pop() + stack.pop()
                stack.append(total)
            elif token == '-':
                first, second = stack.pop(), stack.pop()
                stack.append(second - first)
            elif token == '*':
                total = int(stack.pop()) * int(stack.pop())
                stack.append(total)
            elif token == '/':
                first, second = stack.pop(), stack.pop()
                stack.append(int(float(second) / first))
            else:
                stack.append(int(token))
        
        return stack[0]