class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #east brute force O(n^2)
        ans = heights[0]
        n = len(heights)
        for i in range(n):
            curr = heights[i]
            h = curr
            for j in range(i, n):
                h = min(h, heights[j])
                ans = max(ans, h * (j - i + 1))
        return ans