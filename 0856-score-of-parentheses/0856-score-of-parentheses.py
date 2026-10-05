class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        d = 0
        previous = ""
        result = 0

        for c in s:
            if c == "(":
                d += 1
            else:
                d -= 1
            if previous == "(" and c == ")":
                result += (2**d)
            previous = c
        
        return result
        