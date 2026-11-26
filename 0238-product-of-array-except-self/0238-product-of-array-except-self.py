class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        output = [1]*(len(nums))
        prefix = 1
        postfix = 1
        j = len(nums)-1

        for i in range(len(nums)):
            if i == 0 and j == (len(nums)-1):
                continue
            prefix = prefix * nums[i-1]
            output[i] = output[i] * prefix
            j = j - 1
            postfix = postfix * nums[j+1]
            output[j] = output[j] * postfix
        
        return output
