from typing import List


class Solution:


    def __init__(self):
        self.themap = [
        " ",
        "",
        "abc",
        "def",
        "ghi",
        "jkl",
        "mno",
        "pqrs",
        "tuv",
        "wxyz"
        ]

    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        else:
            houzhui = self.letterCombinations(digits[1:])
            res = []
            for i in self.themap[int(digits[0])]:
                if houzhui:
                    for j in houzhui:
                        res.append(i + j)
                else:
                    res.append(i)

        return res


print(Solution().letterCombinations("23"))