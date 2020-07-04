from typing import List


class Solution:

    def __init__(self):
        self.res = []


    def get(self, stack, now_res, left_rem, right_rem):
        """
        对，但是内存消耗太大了
        """
        if left_rem == 0 and right_rem ==0:
            self.res.append(now_res)
            return
        else:
            # 继续铺（
            if left_rem:
                self.get(stack + ['('], now_res + '(', left_rem - 1, right_rem)
            if len(stack):
                # 铺入）, 必须要在有左边的（的时候才可以，因为要pop
                if right_rem:
                    new_stack = stack[:]
                    new_stack.pop()
                    self.get(new_stack, now_res + ')', left_rem, right_rem  - 1)

    def generateParenthesis(self, n: int) -> List[str]:
        self.get([], '', n , n)

        print(self.res)
        return self.res

    class Solution:
        def generateParenthesis(self, n: int) -> List[str]:
            res = []
            cur_str = ''

            def dfs(cur_str, left, right):
                if left == 0 and right == 0:
                    res.append(cur_str)
                    return
                if right < left:
                    return
                if left > 0:
                    dfs(cur_str + '(', left - 1, right)
                if right > 0:
                    dfs(cur_str + ')', left, right - 1)

            dfs(cur_str, n, n)
            return res

Solution().generateParenthesis(3)