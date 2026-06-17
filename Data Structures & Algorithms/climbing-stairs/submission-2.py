class Solution:
    def climbStairs(self, n: int) -> int:
        count = [0] * (n + 1)
        count[1] = 1
        if n >= 2:
            count[2] = 2

        for i in range(3, n + 1):
            count[i] += count[i - 1] + count[i - 2]
        return count[n]