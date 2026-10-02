class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        # Creating the s variable to store the each valid parenthesis
        s = ""
        # This is to store the transient values of s into the list
        result = []
        # To count the open and close brackets
        open = 0
        close = 0
        self.generator(0,s,open,close,n,result)
        return result

    def generator(self,index,s,open,close,n,output):
        # This is to check if n = 2 then no more than two open parenthsis are generated...
        if open > n:
            return
            # We want it to be until 2*n so using this filter as a base condition...
        if index > 2*n:
            return
            # A valid parenthesis will match the below scenario so once it meets this condition, it will append the string...
        if open == close and index == 2*n:
            output.append(s)

        # This is to generate the open parenthesis
        self.generator(index+1,s+"(",open+1,close,n,output)
        if open > close:
            # To add the closing parenthesis, to find a pair of valid parenthesis...
            self.generator(index+1,s+")",open,close+1,n,output)