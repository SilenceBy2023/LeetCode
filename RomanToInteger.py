class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romanchar = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        def chartoint(char):
            return romanchar.get(char, 0)

        result = chartoint(s[0])

        for i in range(1, len(s)):
            pre = chartoint(s[i - 1])
            cur = chartoint(s[i])

            if cur <= pre:
                result += cur
            else:
                result = result - pre * 2 + cur

        return result


print(Solution().romanToInt('DCC'))
