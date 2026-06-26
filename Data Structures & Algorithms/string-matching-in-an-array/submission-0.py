class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        for a in words:
            for b in words:
                if a!= b and a in b and a not in ans:
                    ans.append(a)
        return ans