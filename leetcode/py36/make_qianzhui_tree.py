from collections import defaultdict


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tree = defaultdict(dict)

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        now_dict = self.tree
        for i in range(len(word)):
            if word[i] in now_dict:
                now_dict = now_dict[word[i]]
            else:
                now_dict[word[i]] = {}
                now_dict = now_dict[word[i]]
            if i == len(word) - 1:
                now_dict["end"] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        now_dict = self.tree
        for i in range(len(word)):
            if word[i] in now_dict:
                now_dict = now_dict[word[i]]
            else:
                return False
            if i == len(word) - 1:
                return "end" in now_dict

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        now_dict = self.tree
        for i in range(len(prefix)):
            if prefix[i] in now_dict:
                now_dict = now_dict[prefix[i]]
            else:
                return False
        return True


trie = Trie()
trie.insert("apple")
print(trie.search("apple"))
print(trie.search("app"))
print(trie.startsWith("app"))
