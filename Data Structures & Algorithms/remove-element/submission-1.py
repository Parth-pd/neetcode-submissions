class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        l = len(nums) - 1
        while i < l:
            if nums[i] == val:
                while i < l and nums[l] == val:
                    l -= 1
                nums[i], nums[l] = nums[l], nums[i]
                l -= 1
            i += 1
        return (l + 1 if l > 0 else 0)

                