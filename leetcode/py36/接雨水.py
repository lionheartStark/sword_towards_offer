from typing import List


# 方法3：
class Solution:
    def trap(self, height: List[int]) -> int:
        """
        双指针，指向从左，从右的当前最高， 算出来后减去最大矩形
        """
        lmax, rmax, res = 0, 0, 0
        for i in range(len(height)):
            lmax = max(lmax, height[i])
            rmax = max(rmax, height[-1 - i])
            res += lmax + rmax - height[i]
        return res - lmax * len(height)

    def trap_stack(self, height: List[int]) -> int:
        """
        单调栈
        """
        length = len(height)
        if length < 3: return 0
        res, idx = 0, 0
        stack = []
        while idx < length:
            while len(stack) > 0 and height[idx] > height[stack[-1]]:
                top = stack.pop()  # index of the last element in the stack
                if len(stack) == 0:
                    break
                h = min(height[stack[-1]], height[idx]) - height[top]
                dist = idx - stack[-1] - 1
                res += (dist * h)
            stack.append(idx)
            idx += 1
        return res

    def trap_dp(self, height: List[int]) -> int:
        # 边界条件
        if not height: return 0
        n = len(height)
        maxleft = [0] * n
        maxright = [0] * n
        ans = 0
        # 初始化
        maxleft[0] = height[0]
        maxright[n - 1] = height[n - 1]
        # 设置备忘录，分别存储左边和右边最高的柱子高度
        for i in range(1, n):
            maxleft[i] = max(height[i], maxleft[i - 1])
        for j in range(n - 2, -1, -1):
            maxright[j] = max(height[j], maxright[j + 1])
        # 一趟遍历，比较每个位置可以存储多少水
        for i in range(n):
            if min(maxleft[i], maxright[i]) > height[i]:
                ans += min(maxleft[i], maxright[i]) - height[i]
        return ans
