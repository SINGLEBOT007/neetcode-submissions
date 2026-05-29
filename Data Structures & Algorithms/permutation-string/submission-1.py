class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        n1 = len(s1)
        n2 = len(s2)

        if n1>n2: return False

        s1_count = [0] * 26
        s2_count = [0] * 26

        for i in range(n1):#97 is ascii of a
            s1_count[ord(s1[i]) - 97] += 1
            s2_count[ord(s2[i]) - 97] += 1

        if s1_count == s2_count: return True

        for i in range(n1, n2):
            s2_count[ord(s2[i]) - 97] += 1
            s2_count[ord(s2[i-n1]) - 97] -= 1 # i-n1 to account for the values added in the first loop

            if s1_count == s2_count: return True

        return False


        

        