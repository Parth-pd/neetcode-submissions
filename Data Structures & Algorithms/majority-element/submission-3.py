class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #OPTIMAL 
        #Boyer-Moore Voting Algorithm
        res = count = 0
        for n in nums:
            if count == 0:
                res = n
            count += (1 if res == n else -1)
        return res
        