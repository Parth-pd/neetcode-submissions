class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ans = 0
        for c in tokens:
            if len(c) > 1 or ord(c) >= ord('0') and ord(c) <= ord('9'):
                stack.append(int(c))
            else:
                a = stack.pop()
                b = stack.pop()
                if c == '+':
                    new = b + a
                elif c == '-':
                    new = b - a
                elif c == '*':
                    new = b * a
                elif c == '/':
                    new = int(b / a)
                stack.append(new)

        return int(stack[-1])