class Solution:
    def maxDepth(self, s: str) -> int:
        transient, maxi = 0,0
        for c in s:
            # To get the running total of "("
            if c == "(":
                transient += 1
            elif c == ")":
                # Once we reach at ")", we would know a particular nesting is complete or a bracket has ended, so find the max then remove the transient value.
                maxi = max(maxi,transient)
                transient -= 1
        
        return maxi
        