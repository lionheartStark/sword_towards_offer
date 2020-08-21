class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        word_list = [[] for _ in range(numRows)]

        count = 0
        for word in s:
            if count <= numRows - 1:
                word_list[count].append(word)
                if count == numRows - 1 and numRows < 3:
                    count = 0
                    continue
                count += 1

            elif count <= 2 * numRows - 3:
                word_list[(numRows - 1) - (count - (numRows - 1))].append(word)
                if count == 2 * numRows - 3:
                    count = 0
                else:
                    count += 1
        res = ''
        for i in word_list:
            for j in i:
                res = res + j
        return res


print(Solution().convert("ABC"
                         , 2))
