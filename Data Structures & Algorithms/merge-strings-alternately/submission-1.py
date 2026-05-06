class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        minlen = min(len(word1), len(word2))
        for i in range(minlen):
            res.append(word1[i])
            res.append(word2[i])
        res.append(word1[minlen:])
        res.append(word2[minlen:])
        
        return"".join(res)