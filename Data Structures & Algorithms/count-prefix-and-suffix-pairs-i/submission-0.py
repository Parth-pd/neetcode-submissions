class Solution:

    def isPrefixAndSuffix(self, s1: str, s2: str) -> bool:

        if len(s2) < len(s1):
            return False
        for i in range(len(s1)):
            if s1[i] != s2[i] or s1[i] != s2[len(s2) - len(s1) + i]:
                return False
        return True
        
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        ans = 0
        n = len(words)
        for i in range(n):
            for j in range(i + 1, n):
                if self.isPrefixAndSuffix(words[i], words[j]):
                    ans += 1
        return ans

    