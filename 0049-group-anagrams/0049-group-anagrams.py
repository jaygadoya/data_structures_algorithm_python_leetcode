class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = []
        hashBuilder = {}
        for each in strs:
            arr = ["0"]*26
            for letter in each:
                arr[ord(letter)-ord("a")] = str(int(arr[ord(letter)-ord("a")]) + 1)
            strBuilder = "#".join(arr)
            if strBuilder not in hashBuilder:
                hashBuilder[strBuilder] = [each]
            else:
                hashBuilder[strBuilder].append(each)

        for key, value in hashBuilder.items():
            temp.append(value)
        
        return temp