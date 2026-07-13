class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        curr = -1
        n = len(t)
        for ch in s:
            while curr < n - 1 and t[curr + 1] != ch:
                curr += 1
            curr += 1
        if curr >= n:
            return False
        return True