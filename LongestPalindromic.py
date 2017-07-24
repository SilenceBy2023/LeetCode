#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Solution(object):
    # 该穷举法运行时间较长，较长字符串时会出现超时现象
    # def longestPalindrome(self, s):
    #     """
    #     :type s: str
    #     :rtype: str
    #     """
    #     mlength, left, right = 0, 0, 0
    #     for i in range(len(s)):
    #         j = i + 1
    #         while j < len(s):
    #             if self.isPaildrome(s, i, j):
    #                 if (j - i + 1) > mlength:
    #                     mlength = j - i + 1
    #                     left = i
    #                     right = j
    #             j += 1
    #     return s[left:right + 1]
    #
    # def isPaildrome(self, s, start, end):
    #     while start < end:
    #         if s[start] != s[end]:
    #             return False
    #         else:
    #             start += 1
    #             end -= 1
    #     return True
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        maxL, maxR, max = 0, 0, 0
        for i in range(n):
            # 长度为偶数的回文字符串
            start = i
            end = i + 1
            while start >= 0 and end < n:
                if s[start] == s[end]:
                    if end - start + 1 > max:
                        max = end - start + 1
                        maxL = start
                        maxR = end
                    start -= 1
                    end += 1
                else:
                    break

            # 长度为奇数的回文子串
            start = i - 1
            end = i + 1
            while start >= 0 and end < n:
                if s[start] == s[end]:
                    if end - start + 1 > max:
                        max = end - start + 1
                        maxL = start
                        maxR = end
                    start -= 1
                    end += 1
                else:
                    break
        return s[maxL:maxR + 1]


if __name__ == '__main__':
    result = Solution().longestPalindrome(
        "ababababababababababababababababababababababababababababababababababababababababababababababababababababababababab")
    print result
