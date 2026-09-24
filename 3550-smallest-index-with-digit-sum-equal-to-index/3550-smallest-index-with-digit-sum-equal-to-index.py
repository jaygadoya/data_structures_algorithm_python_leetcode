class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            indx_sum = self.summation(nums[i])
            if indx_sum == i:
                return i
        return -1

    
    def summation(self,number):
        sum = 0
        while number > 0:
            sum += (number%10)
            number = number // 10
        return sum
        