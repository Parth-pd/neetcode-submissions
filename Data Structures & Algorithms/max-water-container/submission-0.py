class Solution:
    def maxArea(self, heights: List[int]) -> int:
        water = 0
        n = len(heights)
        for i in range(n):
            for j in range(i + 1, n):
                currwater = min(heights[i], heights[j]) * (j - i)
                water = max(currwater, water)
        return water