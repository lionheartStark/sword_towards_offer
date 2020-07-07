class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left_count = 0
        res = 0
        now_res = 0
        for i in s:
            if i == '(':
                left_count += 1
            elif i == ')':
                if left_count > 0:
                    left_count -= 1
                    # 此处不应该草率加一
                    now_res += 1
                    res = max(res, now_res)
                elif left_count == 0:
                    left_count = 0
                    now_res = 0

        return 2*res


print(Solution().longestValidParentheses("()(()"))
