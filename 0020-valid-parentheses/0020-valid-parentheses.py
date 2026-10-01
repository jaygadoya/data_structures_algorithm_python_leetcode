class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        open = 0
        close = 0
        for i in s:
            if i == "(" or i == "[" or i == "{":
                stack.append(i)
                open += 1
            elif len(stack) != 0:
                if (stack[-1] + i) == "()" or (stack[-1] + i) == "[]" or (stack[-1] + i) == "{}":
                    stack.pop()
                    close += 1
                else:
                    return False
            else:
                return False
        if open == close:
            return True
        else:
            return False