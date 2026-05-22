class Solution:

    def encode(self, strs: List[str]) -> str:

        code=""

        for word in strs:
            code+= str(len(word))+'#'+word
        
        return code

    def decode(self, s: str) -> List[str]:

        msg=[]
        i=0

        while i<len(s):
            j=i
            while s[j] !='#':
                j+=1
            length = int(s[i:j])
            j+=1
            word = s[j:j+length]
            msg.append(word)
            i=j+length

        return msg

