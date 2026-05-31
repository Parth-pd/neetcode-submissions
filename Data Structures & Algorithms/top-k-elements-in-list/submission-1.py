class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}
        for n in nums:
            h[n] = h.get(n, 0) + 1
        return sorted(h, key=h.get, reverse=True)[:k]