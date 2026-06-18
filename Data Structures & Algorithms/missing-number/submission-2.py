class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        real = 0
        curr = 0
        for i in range(len(nums)):
            real = real ^ i
            curr = curr ^ nums[i]
        real = real ^ len(nums)
        return (real ^ curr)