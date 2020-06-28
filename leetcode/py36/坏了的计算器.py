class Solution:
    """
    在显示着数字的坏计算器上，我们可以执行以下两种操作：

    双倍（Double）：将显示屏上的数字乘 2；
    递减（Decrement）：将显示屏上的数字减 1 。
    最初，计算器显示数字 X。

    返回显示数字 Y 所需的最小操作数。

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/broken-calculator
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """

    def brokenCalc(self, x: int, y: int) -> int:
        self.res = 0

        def my(x, y):
            if x >= y:
                self.res += x - y
            else:
                if y % 2 == 0:
                    my(x, y // 2)
                    self.res += 1
                else:
                    my(x, (y + 1))
                    self.res += 1

        my(x, y)

        return self.res

print(Solution().brokenCalc(2,3))