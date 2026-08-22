class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dups = {}
        for i in range(len(nums)):
            if nums[i] in dups:
                return True
            dups[nums[i]] = 1
        return False
