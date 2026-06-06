class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = []
        for s in strs:
            new = str(len(s)) + '#' + s
            ans.append(new)
        return ("".join(ans))
    def decode(self, s: str) -> List[str]:
        ans = []
        curr = 0
        while curr < len(s):
            ls = int(s[curr])
            while s[curr + 1].isdigit():
                curr += 1
                ls = ls*10 + int(s[curr])
            st = ''
            for i in range(curr + 2, ls + curr + 2):
                st += s[i]
            curr += ls + 2
            ans.append(st)
        return ans
