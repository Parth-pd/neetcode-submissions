class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #brute force LOL
        fleets = defaultdict(list)
        n = len(position)
        
        h ={}
        for i in range(n):
            h[position[i]] = speed[i] 

        correct = dict(sorted(h.items()))

        stack = []
        for i in range(n - 1, -1, -1):

            currpos, currspeed = list(correct.items())[i]
            
            currT = (target - currpos) / currspeed
            if stack:
                lastT = stack.pop()
                if lastT > currT:
                    fleets[lastT].append(i)
                    stack.append(lastT)
                else:
                    fleets[currT].append(i)
                    stack.append(currT)
            else:
                fleets[currT].append(i)
                stack.append(currT)
        return (len(fleets))