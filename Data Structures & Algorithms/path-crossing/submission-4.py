class Solution:
    def isPathCrossing(self, path: str) -> bool:
        positions = [[0,0]]
        N = 0
        E = 0
        for ch in path:
            if ch == 'N':
                N += 1
            elif ch == 'S':
                N -= 1
            elif ch == 'E':
                E += 1
            else:
                E -= 1
            curr = [N,E]
            if curr in positions:
                return True
            positions.append([N,E])
        return False

        