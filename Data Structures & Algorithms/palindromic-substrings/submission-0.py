class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(n):
            for j in range(i, n):
                curr = s[i:j+1]
                if curr == curr[::-1]:
                    ans += 1
        return ans