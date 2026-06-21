class Solution:
    def check(self, nums: List[int]) -> bool:
        i = 0
        x = 0
        n = len(nums)
        first = min(nums)
        while nums[i] != first:
            i += 1
        x = i
        for j in range(n - 1):
            if nums[(j + 1 + x) % n] < nums[(j + x) % n]:
                return False
        return True
            