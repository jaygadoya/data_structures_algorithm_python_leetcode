class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter0 = 0
        counter1 = 0
        counter2 = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                counter0 += 1
            elif nums[i] == 1:
                counter1 += 1
            else:
                counter2 += 1
        temp = -1
        for i in range(0,counter0):
            temp += 1
            nums[i] = 0
        for i in range(0,counter1):
            temp += 1
            nums[temp] = 1
        for i in range(0,counter2):
            temp += 1
            nums[temp] = 2

        