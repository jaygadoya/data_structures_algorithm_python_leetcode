class Solution:
    def compress(self, chars: list[str]) -> int:
        initial = chars[0]
        counter = 0
        s = ""
        for i in range(len(chars)):
            if chars[i] != initial:
                if counter != 1:
                    s = s + initial
                    s = s + str(counter)
                else:
                    s += initial
                counter = 1
            elif chars[i] == initial:
                counter += 1
            if len(chars) - 1 == i:
                if counter == 1:
                    s = s + chars[i]
                else:
                    s = s + chars[i]
                    s = s + str(counter)
            initial = chars[i]

        for i in range(len(s)):
            chars[i] = s[i]

        return len(s)