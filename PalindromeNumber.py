class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        # method 1
        # if x < 0:
        #     return False
        # elif x == 0:
        #     return True
        # b = x
        # ans = 0
        # while x > 0:
        #     ans = ans * 10 + x % 10
        #     if x > 2147483647:
        #         return False
        #     x //= 10
        # if ans == b:
        #     return True
        # return False

        # method 2
        s = str(x)
        return s == str(s[::-1])


print(Solution().isPalindrome(12321))
