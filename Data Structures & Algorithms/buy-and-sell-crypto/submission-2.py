class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        n = len(prices)
        pre = [prices[0]]
        post = [prices[n - 1]]
        
        for i in range(n):
            pre.append(min(pre[-1], prices[i]))
            post.append(max(post[-1], prices[n - 1 - i]))
        for i in range(1, n + 1):
            profit = max(profit, (post[n - i] - pre[i]))
        return max(profit, 0)