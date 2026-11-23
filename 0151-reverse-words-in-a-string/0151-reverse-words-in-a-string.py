class Solution:
    def reverseWords(self, s: str) -> str:
        input = s.split()
        i = 0
        j = len(input)-1
        while i < j:
            input[i], input[j] = input[j], input[i]
            i += 1
            j -= 1
        return " ".join(input)
    
        