class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #two pointers solution
        l, r = 0, len(heights) - 1
        water = 0
        while l < r:
            curr = min(heights[l], heights[r]) * (r - l)
            water = max(water, curr)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return water