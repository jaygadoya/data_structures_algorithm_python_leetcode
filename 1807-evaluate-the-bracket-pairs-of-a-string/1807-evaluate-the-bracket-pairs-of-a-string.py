class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        container = {}
        for i in knowledge:
            container[i[0]] = i[1]
        print(container)

        output = ""
        temp = ""
        flag = False
        for i in range(0,len(s)):
            if s[i] == "(":
                flag = True
            elif s[i] == ")":
                flag = False
                if temp in container:
                    output += container[temp]
                else:
                    output += "?"
                temp = ""
            elif flag:
                temp += s[i]
            else:
                output += s[i]

        return output
        