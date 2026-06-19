class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid[0])
        freq = [0] * (n ** 2 + 1)
        for row in grid:
            for x in row:
                freq[x] += 1
        missing = 0
        repeated = 0
        for i in range(1, (n ** 2) + 1):
            if freq[i] == 2:
                repeated = i
            elif freq[i] == 0:
                missing = i
        return [repeated, missing]
