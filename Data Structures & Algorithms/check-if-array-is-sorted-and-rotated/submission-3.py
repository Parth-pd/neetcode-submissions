class Solution:
    def check(self, nums: List[int]) -> bool:
        i = 0
        x = 0
        n = len(nums)
        real = sorted(nums)
        while nums[i] != real[0]:
            i += 1
        x = i
        for j in range(n):
            if real[j] != nums[(j + x) % n]:
                return False
        return True
            