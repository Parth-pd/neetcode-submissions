class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        if len(s) % 2 == 1:
            return False
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                st.append(s[i])
            else:
                curr = s[i]
                try:
                    recent = st.pop()
                except:
                    return False
                mix = recent + curr
                if mix == "()" or mix == "{}" or mix == "[]":
                    continue
                else:
                    return False
        return (True if len(st) == 0 else False)