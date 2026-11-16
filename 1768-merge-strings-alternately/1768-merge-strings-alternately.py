class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = len(word1)
        m = len(word2)
        left = 0
        right = 0
        output = ""
        while left < n and right < m:
            output = output + word1[left]
            output = output + word2[right]
            left += 1
            right += 1
        
        while left < n:
            output = output + word1[left]
            left += 1
        
        while right < m:
            output = output + word2[right]
            right += 1

        return output
        
