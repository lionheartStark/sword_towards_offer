from typing import List
import collections
import functools

class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        dict.sort()
        words = sentence.split(" ")
        res = ""
        a = 1
        for word in words:
            is_root = False
            for root in dict:
                if str(word).startswith(root):
                    res = res + root + " "
                    is_root = True
                    break
            if not is_root:
                res = res + word + " "
        return res[:-1]

    def replaceWords(self, roots, sentence):
        rootset = set(roots)

        def replace(word):
            for i in (1, len(word)):
                if word[:i] in rootset:
                    return word[:i]
            return word

        return " ".join(map(replace, sentence.split()))

    def replaceWords(self, roots, sentence):
        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()
        END = True

        for root in roots:
            functools.reduce(dict.__getitem__, root, trie)[END] = root

        def replace(word):
            cur = trie
            for letter in word:
                if letter not in cur or END in cur: break
                cur = cur[letter]
            return cur.get(END, word)

        return " ".join(map(replace, sentence.split()))

print(Solution().replaceWords(roots=["cat", "bat", "rat"], sentence="the cattle was rattled by the battery"))
