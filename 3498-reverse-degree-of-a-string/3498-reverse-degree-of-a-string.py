class Solution:
    def reverseDegree(self, s: str) -> int:
        sum = 0
        for i in range(len(s)):
            # Here the number 123 is found out by adding 26 to the ascii value of the a, this will give us a to be 26 and z to be 1.
            sum += ((123-ord(s[i]))*(i+1))
            # Later multiplying the values with (index+1) as that is what is being stated in the question.
            # Post it we are just rolling up the sum.
        
        return sum

        