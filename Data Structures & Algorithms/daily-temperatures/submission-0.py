class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #brute force
        result = []
        n = len(temperatures)
        for i in range(n):
            curr = temperatures[i]
            day = i
            while day < n and not temperatures[day] > curr:
                if day == n- 1:
                    day = i
                    break
                day += 1
            result.append(day - i)
        return result