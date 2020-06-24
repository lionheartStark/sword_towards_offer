import math
class Solution:
    def lastSubstring(self, s: str) -> str:
        stack = ""
        j = 0
        for i in s:
            if stack == "":
                stack= i
            else:
                if i > stack[0]:
                    stack = i
                    j = 0
                elif i == stack[0]:
                    if stack[-1] == i:
                        stack += i
                        new = stack[j: len(stack)]
                        if new > stack[0:len(new)]:
                            stack = new
                            j = 0
                    else:
                        stack += i
                        j = len(stack)-1
                else:
                    stack += i
                    if j:
                        new = stack[j: len(stack)]
                        if new > stack[0:len(new)]:
                            stack = new
                            j = 0

        print(stack)
        return stack

Solution().lastSubstring("zzzwzzzz")