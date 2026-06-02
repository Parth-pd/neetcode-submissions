class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        ans = 0
        for n in nums:
            if n - 1 not in s:
                curr = n
                streak = 1
                while curr + 1 in s:
                    curr += 1
                    streak += 1
                ans = max(ans, streak)

        return ans
                