class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = 1
        if (dividend > 0 and divisor > 0) or (dividend > 0 and divisor > 0):
            sign = 1
        elif (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            sign = -1
        dividend, divisor, a, b = abs(dividend), abs(divisor), 0, 1
        if dividend < divisor:
            return 0
        while dividend >= divisor:
            if dividend >= b * divisor:
                dividend -= b * divisor
                a += b
                b += 1
            else:
                b -= 1
        if a * sign > 2 ** 31 - 1 or a * sign < -2 ** 31:
            return 2 ** 31 - 1
        return a * sign
