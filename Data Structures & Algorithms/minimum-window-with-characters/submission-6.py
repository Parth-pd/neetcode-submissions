class Solution:
    def minWindow(self, s: str, t: str) -> str:
        req = dict(Counter(t))
        curr = {}
        n = len(s)
        ans = ""
        l,r = 0, 0
        while r < n:
            if all(curr.get(k, 0) >= v for k, v in req.items()):
                if ans == "" or len(ans) > r - l:
                    ans = s[l:r]
                x = req.get(s[l], 0)
                if curr.get(s[l], 0) != 0:
                    if x == 0:
                        del curr[s[l]]
                    else:
                        curr[s[l]] -= 1
                l += 1
            else:
                ch = s[r]
                if ch in req:
                    curr[ch] = curr.get(ch, 0) + 1
                r += 1

        while all(curr.get(k, 0) >= v for k, v in req.items()):
            if ans == "" or len(ans) > r - l:
                ans = s[l:r]
            ch = s[l]
            if ch in curr:
                curr[ch] -= 1
                if curr[ch] == 0:
                    del curr[ch]
            l += 1
                
        return ans


