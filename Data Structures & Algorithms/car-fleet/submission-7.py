class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #Optimal Solution:
        h = {}
        for i in range(len(position)):
            h[position[i]] = speed[i]
        sortedCars = dict(sorted(h.items(), reverse=True))

        stack = []
        for p, s in sortedCars.items():
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)