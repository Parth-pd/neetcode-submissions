class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1 = len(word1)
        n2 = len(word2)
        m = min(n1, n2)
        ans = ['.'] * (2* m)
        
        for i in range(m):
            ans[2*i] = word1[i]
            ans[2*i + 1] = word2[i]
        if n1 > n2:
            return "".join(ans) + word1[m::]
        else:
            return "".join(ans) + word2[m::]
