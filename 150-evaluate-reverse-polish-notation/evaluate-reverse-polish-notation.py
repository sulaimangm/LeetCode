class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == "+":
                stack.append(int(stack.pop()) + int(stack.pop()))
            elif i == "*":
                stack.append(int(stack.pop()) * int(stack.pop()))
            elif i == "-":
                temp = int(stack.pop())
                stack.append(int(stack.pop()) - temp)
            elif i == "/":
                temp = float(stack.pop())
                stack.append(int(float(stack.pop()) / temp))
            else:
                stack.append(i)
        return int(stack[0])