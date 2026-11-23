class Solution:
    def reverseVowels(self, s: str) -> str:
        hashContainer = {'a','e','i','o','u','A','E','I','O','U'}
        input = list(s)
        i = 0
        j = len(input)-1

        while i < j:
            if input[i] in hashContainer and input[j] in hashContainer:
                input[i], input[j] = input[j], input[i]
                i += 1
                j -= 1
            elif input[i] in hashContainer and input[j] not in hashContainer:
                j -= 1
            elif input[i] not in hashContainer and input[j] in hashContainer:
                i += 1
            elif input[i] not in hashContainer and input[j] not in hashContainer:
                i += 1
                j -= 1
        return "".join(input)