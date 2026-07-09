class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        for i in range(0, len(nums) - k + 1):
            curr = nums[i]
            for j in range(i, i + k):
                curr = max(nums[j], curr)
            ans.append(curr)
        return ans