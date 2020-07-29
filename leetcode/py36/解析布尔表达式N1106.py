class Solution:

    def get_op(self, op, args):
        if op == "&":
            ans = not (False in args)
        if op == "|":
            ans = True in args
        if op == "!":
            ans = not args[0]
        return ans

    def parseBoolExpr(self, expression: str) -> bool:
        stack = []
        tmp = []
        for i in expression:
            # 常规的就入栈
            if i == ",":
                continue
            elif i == "t":
                stack.append(True)
            elif i == "f":
                stack.append(False)
            elif i == ")":
                while stack and stack[-1]!= "(":
                    tmp.append(stack.pop())

                # 弹出左括号
                stack.pop()
                # 弹出操作符
                op = stack.pop()
                ans = self.get_op(op, tmp)
                stack.append(ans)
                tmp = []
            else:
                stack.append(i)
        return stack[0]