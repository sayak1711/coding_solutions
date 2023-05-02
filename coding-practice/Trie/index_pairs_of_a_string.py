# https://leetcode.com/problems/index-pairs-of-a-string/
class Trie:
    def __init__(self):
        self.root = {}
        self.end = '*'
    
    def insert(self, word):
        t = self.root

        for c in word:
            if c in t:
                t = t[c]
            else:
                t[c] = {}
                t = t[c]
        t[self.end] = True
        

class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        i, l = 0, len(text)
        trie = Trie()
        for word in words:
            trie.insert(word)
        result = []

        while i < l:
            j = i
            p = trie.root
            while j < l:
                if text[j] not in p:
                    break
                p = p[text[j]]
                if '*' in p:
                    result.append([i, j])
                j += 1
            i += 1
        return result