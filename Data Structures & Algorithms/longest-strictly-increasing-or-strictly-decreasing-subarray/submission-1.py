class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        i = 0
        j = 0
        n = len(nums)
        ans = min(1, n)
        while i + 1 < n and j < n:
            curr = nums[i]
            if curr < nums[i + 1]:
                j = i + 1
                while j < n and nums[j] > nums[j - 1]:
                    j += 1
                ans = max(ans, j - i)
            elif curr > nums[i + 1]:
                j = i + 1
                while j < n and nums[j] < nums[j - 1]:
                    j += 1
                ans = max(ans, j - i)
            i += 1
        return ans
