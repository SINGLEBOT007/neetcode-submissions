class Solution:
    def isValid(self, s: str) -> bool:
        stc = []
        closeMap = {")":"(", "}":"{", "]":"["}

        for i in s:
            if i in closeMap:
                if stc and stc[-1] == closeMap[i]:
                    stc.pop()
                else:
                    return False
            else:
                stc.append(i)
        return True if not stc else False