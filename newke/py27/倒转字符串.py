class Solution:
    def ReverseSentence(self, s):
        k = s.split(" ")
        k = k[::-1]
        astr = ""
        for i in k:
            astr+=i+" "
        return astr[:-1]

Solution().ReverseSentence("student a am I")