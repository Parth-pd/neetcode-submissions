class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        h = {}
        highest = 0
        ans = 0
        for x in nums:
            h[x] = h.get(x, 0) + 1
            if h[x] > highest:
                highest = h[x]
                ans = x
        return ans
        
        