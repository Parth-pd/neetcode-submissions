class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [1]
        post = [1]
        for i in range(n):
            pre.append(pre[i] * nums[i])
            post.append(post[i] * nums[n - i - 1])

        ans = []
        for i in range(n):
            mult = pre[i] * post[n - i - 1]
            ans.append(mult)
        return ans