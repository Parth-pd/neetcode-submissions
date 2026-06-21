class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans = [0] * 2
        for x in nums:
            x = abs(x)
            if nums[x - 1] < 0:
                ans[0] = x
            nums[x - 1] = -nums[x - 1]

        for i, n in enumerate(nums):
            if n > 0 and i + 1 != ans[0]:
                ans[1] = i + 1
        return ans