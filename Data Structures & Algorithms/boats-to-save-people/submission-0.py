class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        ppl = sorted(people)
        l,r = 0, len(ppl)-1
        c = 0

        while l<=r:
            if ppl[l] == limit:
                l+=1
                c+=1
            elif ppl[r] == limit:
                r-=1
                c+=1
            elif ppl[l] + ppl[r] <= limit:
                l+=1
                r-=1
                c+=1
            else:
                r-=1
                c+=1
        return c
