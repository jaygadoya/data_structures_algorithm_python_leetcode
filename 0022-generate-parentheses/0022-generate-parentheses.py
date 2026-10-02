class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        s = ""
        result = []
        open = 0
        close = 0
        self.generator(0,s,open,close,n,result)
        return result

    def generator(self,index,s,open,close,n,output):
        if open > n:
            return
        if index > 2*n:
            return
        if open == close and index == 2*n:
            output.append(s)

        self.generator(index+1,s+"(",open+1,close,n,output)
        if open > close:
            self.generator(index+1,s+")",open,close+1,n,output)