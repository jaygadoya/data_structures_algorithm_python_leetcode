class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        for zeroth in range(len(nums)):
            if nums[zeroth] == 0:
                i = zeroth
                break
        if i == len(nums)-1:
            return
        for nonZeroth in range(i,len(nums)):
            if nums[nonZeroth] != 0:
                j = nonZeroth
                break
        if j == 0:
            return
        while (i < len(nums)) and (j < len(nums)):
            if nums[i] != 0:
                i += 1
            elif nums[j] == 0:
                j += 1
            elif nums[i] == 0 and nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
        
                
        