class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charHash = {}
        if len(s) != len(t):
            return False
        for indx in range(len(s)):
            if s[indx] not in charHash:
                charHash[s[indx]] = 1
            elif s[indx] in charHash:
                charHash[s[indx]] += 1
            if t[indx] not in charHash:
                charHash[t[indx]] = -1
            elif t[indx] in charHash:
                charHash[t[indx]] -= 1

        for key, value in charHash.items():
            if value != 0:
                return False
        return True
            
              