class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        temp = []
        for i in range(len(nums)):
            if nums[i] < 0:
                neg.append(nums[i])
            else:
                pos.append(nums[i])
        for i in range(len(pos)):
            temp.append(pos[i])
            temp.append(neg[i])

        return temp