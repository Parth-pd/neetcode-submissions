class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        freqS = [0] * 26
        freqT = [0] * 26
        for ch in s:
            freqS[ord(ch) - ord('a')] += 1
        for ch in t:
            freqT[ord(ch) - ord('a')] += 1
        for i in range(26):
            if freqS[i] != freqT[i]:
                return chr(i + ord('a'))