class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        ans = 0
        for c in s[::-1]:
            if c == ' ':
                break
            ans += 1
        return ans