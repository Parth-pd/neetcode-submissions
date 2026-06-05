class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        zeros = nums.count(0)
        mult = 1
        if zeros > 1:
            return ([0] * (len(nums)))
        for x in nums:
            if x != 0:
                mult *= x
        ans = []
        for x in nums:
            if x == 0:
                ans.append(mult)
            elif zeros == 1:
                ans.append(0)
            else:
                ans.append(mult // x)
        return ans
        