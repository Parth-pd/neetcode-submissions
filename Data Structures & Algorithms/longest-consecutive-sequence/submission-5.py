class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        l = len(nums)
        if l <= 1:
            return l
        ans = 1
        for i in range(l):
            curr = nums[i]
            for j in range(i + 1, l):
                if nums[j] - curr == 1:
                    curr = nums[j]
                    ans = max(ans, j - i + 1)
                else:
                    break
        return ans