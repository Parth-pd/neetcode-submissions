class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        freq = [0] * (len(nums) + 1)
        for x in nums:
            freq[x] += 1
        missing = 0
        repeat = 0
        for i in range(len(nums) + 1):
            if freq[i] == 0:
                missing = i
            elif freq[i] == 2:
                repeat = i
        return [repeat, missing]