class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        small = (2**31) + 1
        medium = (2**31) - 1
        for i in range(0,len(nums)):
            if nums[i] <= small:
                small = nums[i]
            elif nums[i] <= medium:
                medium = nums[i]
            else:
                return True
        return False