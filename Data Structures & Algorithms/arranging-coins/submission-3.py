class Solution:
    def arrangeCoins(self, n: int) -> int:
        ans = 0
        l, r = 0, n
        while l <= r:
            mid = (l + r) // 2
            curr = mid * (mid + 1) // 2
            if curr <= n:
                ans = max(ans, mid)
                l = mid + 1
            else:
                r = mid - 1
        return ans