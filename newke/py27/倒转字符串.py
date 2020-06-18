class Solution:
    def ReverseSentence(self, s):
        k = s.split(" ")
        k = k[::-1]
        astr = ""
        for i in k:
            if len(i) > 0:
                astr += i+" "
        return astr[:-1]

print([Solution().ReverseSentence("  hello world!  ")])