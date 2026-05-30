class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = []
        ans = []
        for s in strs:
            h = {}
            for ch in s:
                h[ch] = h.get(ch, 0) + 1
            count.append(h)
        i = 0
        while i < len(strs):
            curr = []
            curr.append(strs[i])
            j = i + 1
            while j < len(strs):
                if count[i] == count[j]:
                    curr.append(strs[j])
                    strs.pop(j)
                    count.pop(j)
                else:
                    j += 1
            ans.append(curr)
            i += 1
        return ans