class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        prefix = [0] * (n + 1) # using prefix sum
        # prefix[i] is sum of first i elements
        
        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] + nums[i - 1]
        maxL = 1
        right = 0
        left = 0
        while left <= right and right < n:
            window_sum = prefix[right + 1] - prefix[left]
            size = right - left + 1
            cost = nums[right] * size - window_sum
            if cost <= k:
                maxL = max(maxL, size)
                right += 1
            else:
                left += 1
        return maxL