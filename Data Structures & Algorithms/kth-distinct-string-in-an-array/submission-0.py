class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d = []
        count = Counter(arr)
        for s in arr:
            if count[s] == 1:
                d.append(s)

        try:
            return d[k - 1]
        except:
            return ""