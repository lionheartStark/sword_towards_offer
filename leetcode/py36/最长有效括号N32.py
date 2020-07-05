class Solution:
    def longestValidParentheses_dp(self, s: str) -> int:
        # 状态：以该点结尾的最长有效括号的子串长度
        dp = [0 for _ in range(len(s))]
        if len(s) < 2:
            return 0

        if s[1] == ')' and s[0] == '(':
            dp[1] = 2

        if len(s) == 2:
            return dp[1]

        for i in range(2, len(s)):
            if s[i] == '(':  ## 一种情况
                dp[i] = 0
                continue
            if s[i] == ')':  ## 另一种情况
                if s[i - 1] == '(':  ## 细分
                    dp[i] = dp[i - 2] + 2
                if s[i - 1] == ')' and s[i - 1 - dp[i - 1]] == '(' and i - 1 - dp[i - 1] >= 0:  ## 复杂的一种情况，需要特判
                    dp[i] = dp[i - 1 - dp[i - 1] - 1] + 2 + dp[i - 1]
        print(dp)
        return max(dp)


    def longestValidParentheses_stack(self, s: str) -> int:
        ans = 0  # 最大合法长度(返回值)
        stack = [-1, ]  # stack[0]:合法括号起点-1 ; stack[1:]尚未匹配左括号下标
        for i, ch in enumerate(s):
            if '(' == ch:  # 左括号
                stack.append(i)
            elif len(stack) > 1:  # 右括号，且有成对左括号
                stack.pop()  # 成对匹配
                ans = max(ans, i - stack[-1])
            else:  # 非法的右括号
                stack[0] = i
        return ans
