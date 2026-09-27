class Solution:
    def reverseParentheses(self, s: str) -> str:
        # Using a stack to reverse the strings which are part of the given value
        # Easier, as we want to get the string in reverse order.
        stack = []

        # Iterating through each character.
        for c in s:
            # The if condition statement is to stop at the character = "("
            if c == ")":
                portion = []
                # Initializing a list to store intermediate results.

                # This loop is to pop out the values until we reach the character "("
                while stack[-1] != "(":
                    portion.append(stack.pop())
                # We want to remove the "(" from the stack so we are popping it once again.
                stack.pop()
                # Rather than using a for loop here to append the characters in stack using the extend function to make the code be cleaner.
                stack.extend(portion)

            # This conditional statement will handle the part where we want to append the characters until we reach "("
            else:
                stack.append(c)

            # This is to return the answer in form of a string from a stack so using the join function.
            # Here the stack will get values from 0 to N-1, i.e. N = Length of the list.
        return "".join(stack)
        