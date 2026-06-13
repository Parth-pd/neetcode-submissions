class Solution:
    def trap(self, height: list[int]) -> int:
        if not height:
            return 0
            
        n = len(height)
        maxleft = [0] * n
        maxright = [0] * n
        
        # 1. Populate maxleft from left to right
        maxleft[0] = height[0]
        for i in range(1, n):
            maxleft[i] = max(maxleft[i - 1], height[i])
            
        # 2. Populate maxright from right to left
        maxright[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            maxright[i] = max(maxright[i + 1], height[i])
            
        # 3. Calculate trapped water
        water = 0
        for i in range(n):
            # The water level is limited by the shorter of the two walls
            water_level = min(maxleft[i], maxright[i])
            # Trapped water is the level minus the bar's own height
            water += water_level - height[i]
            
        return water