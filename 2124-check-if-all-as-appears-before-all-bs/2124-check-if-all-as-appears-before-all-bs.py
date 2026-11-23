class Solution:
    def checkString(self, s: str) -> bool:
        isAFlag = True
        isBFlag = False
        for i in range(0,len(s)):
            if s[i] == 'b':
                isBFlag = True
            elif s[i] == 'a' and isBFlag == True:
                return False
        
        
        return isAFlag
        