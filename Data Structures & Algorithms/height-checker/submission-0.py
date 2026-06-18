class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        ex = heights.copy()
        ex.sort()
        ans = 0
        for i in range(len(ex)):
            if ex[i] != heights[i]:
                ans += 1
        return ans