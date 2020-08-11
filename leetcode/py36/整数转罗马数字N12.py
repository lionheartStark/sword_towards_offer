class Solution:
    def intToRoman(self, num: int) -> str:
        num_str = str(num)
        count = 0
        ans = ""
        the_map = {0: {0: '', 1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX'},
                   1: {0: '', 1: 'X', 2: 'XX', 3: 'XXX', 4: 'XL', 5: 'L', 6: 'LX', 7: 'LXX', 8: 'LXXX', 9: 'XC'},
                   2: {0: '', 1: 'C', 2: 'CC', 3: 'CCC', 4: 'CD', 5: 'D', 6: 'DC', 7: 'DCC', 8: 'DCCC', 9: 'CM'},
                   3: {0: '', 1: 'M', 2: 'MM', 3: 'MMM', }
                   }
        for a_num_str in num_str[::-1]:
            now_str = the_map[count][int(a_num_str)]
            ans = now_str + ans
            count += 1
        return ans


class Solution:
    def intToRoman(self, num: int) -> str:
        the_map = {
            1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C",
            90: "XC", 50: "L", 40: "XL",
            10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I",

        }
        res = ""
        for k, v in the_map.items():
            while num - k >= 0:
                res += v
                num -= k
        return res


ans = Solution().intToRoman(1994)
print(ans)
