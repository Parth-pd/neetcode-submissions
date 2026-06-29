class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left = 0
        right = total - nums[0]

        for i in range(len(nums)):
            if i > 0:
                left += nums[i - 1]
                right -= nums[i]
            if left == right:
                return i 
        return -1