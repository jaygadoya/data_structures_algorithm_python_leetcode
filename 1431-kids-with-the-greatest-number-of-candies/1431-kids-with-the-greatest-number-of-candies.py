class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        maxCandies = 0
        output = []
        for i in range(0,len(candies)):
            if candies[i] > maxCandies:
                maxCandies = candies[i]

        for j in range(0,len(candies)):
            if candies[j] + extraCandies >= maxCandies:
                output.append(True)
            else:
                output.append(False)
        
        return output
        