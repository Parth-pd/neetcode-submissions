class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        
        diff = []
        for i in range(n - 1):
            diff.append(nums[i + 1] - nums[i])
        i = 0
        j = 0
        maxL = 1
        while i < n - 1:
            j = i
            rem = k #currently we have done 0 operations
            while j < n - 1 and rem >= diff[j] * (j - i + 1):
                rem -= diff[j] * (j - i + 1)
                j += 1
            maxL = max(j - i + 1, maxL)
            i += 1
        return maxL

