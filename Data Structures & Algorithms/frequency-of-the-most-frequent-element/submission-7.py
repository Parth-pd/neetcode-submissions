class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        maxL = 1
        right = 0
        left = 0
        total = nums[0]
        while left <= right and right < n:
            size = right - left + 1
            cost = nums[right] * size - total
            if cost <= k:
                maxL = max(maxL, size)
                if right < n - 1:
                    total += nums[right + 1]
                right += 1
            else:
                total -= nums[left]
                left += 1
        return maxL