class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = []
        l = 0
        strs.sort(key=len)
        smallest = strs[0]
        total = len(strs)
        for i in range(len(smallest)): #smallest string
            curr = smallest[i]
            count = 0
            for s in strs:
                if curr == s[i]:
                    count += 1
                else:
                    break
            if count != total:
                break
            l = i + 1
        return smallest[:l]
                    
            