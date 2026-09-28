class Solution:
    def maxDepth(self, s: str) -> int:
        transient, maxi = 0,0
        for c in s:
            if c == "(":
                transient += 1
            elif c == ")":
                maxi = max(maxi,transient)
                transient -= 1
        
        return maxi
        