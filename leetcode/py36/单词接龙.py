import string
class Solution:
    def __init__(self):
        self.keylist = {}
        self.res = []
        self.find = False
        self.end = None
        self.can_trans_map = {}

    def can_trans(self, left, wordList):
        # if f"{left}_{right}" in self.can_trans_map:
        #     return self.can_trans_map[f"{left}_{right}"]
        # else:
        #     keylist = [1 for i in range(len(left)) if left[i] != right[i]]
        #     if keylist.count(1) == 1:
        #         self.can_trans_map[f"{left}_{right}"] = right
        #         return right
        #     else:
        #         self.can_trans_map[f"{left}_{right}"] = None
        #         return None
        theset =set()
        left_list = list(left)
        for j in range(len(left)):

            origin_char = left_list[j]

            for k in string.ascii_lowercase:
                left_list[j] = k
                next_word = ''.join(left_list)
                if next_word == origin_char:
                    continue
                if next_word in wordList:
                    theset.add(next_word)
            left_list[j] = origin_char
        return theset

    def find_xulie(self, key, nowlist):
        anowlist = nowlist[:] +[key]
        if self.end in anowlist:
            self.res.append(anowlist)
        else:
            if key in self.keylist:
                for i in self.keylist[key]:
                    self.find_xulie(i, anowlist)


    def findLadders(self, beginWord: str, endWord: str, wordList: [str]) -> [[str]]:
        #wordList = [TreeNode(i) for i in (set(wordList)-set(beginWord))]
        self.end = endWord
        wordList = set(wordList)
        can_remove = {beginWord}
        thislayer = {beginWord}
        if not wordList or not endWord in wordList:
            return []

        while True:

            wordList = wordList -can_remove

            can_remove = set()
            for j in thislayer:
                if not (j in self.keylist):
                    self.keylist[j] = set()
                j_kid = set()

                a = self.can_trans(j, wordList)
                if a:
                    j_kid |= a
                    if endWord in a:
                        self.find = True
                self.keylist[j] = self.keylist[j] | set(j_kid)
                can_remove = can_remove|(j_kid)

            thislayer = can_remove
            if not thislayer or endWord in thislayer:
                break
        if not self.find:
            return []
        else:
            self.find_xulie(beginWord, [])
            return self.res



#print(Solution().can_trans("dog","lkg"))
print(Solution().findLadders(
"hit","cog",["hot","dot","dog","lot","log","cog"]
))