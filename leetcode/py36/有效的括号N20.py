class Solution:
    def isValid(self, s: str) -> bool:
        map = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        stack = []
        for i in s:
            if i in ['(', '[', '{']:
                stack.append(i)
            elif i in [')', ']', '}']:
                if stack == []:
                    return False
                elif map[stack[-1]] != i:
                    return False
                else:
                    stack.pop()
        return len(stack) == 0


print(Solution().isValid("}"))
