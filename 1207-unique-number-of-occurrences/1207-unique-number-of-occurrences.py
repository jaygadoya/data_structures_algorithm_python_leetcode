class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        container = {}
        for i in range(len(arr)):
            if arr[i] not in container:
                container[arr[i]] = 1
            else:
                container[arr[i]] += 1
        
        s = set()
        for key, value in container.items():
            if value not in s:
                s.add(value)
            else:
                return False
        
        return True
        