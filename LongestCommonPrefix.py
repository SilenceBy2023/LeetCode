class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # import os
        # return os.path.commonprefix(strs)

        if not strs:
            return ''
        cur = ''
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[j][i] != strs[0][i]:
                    return cur
            cur += strs[0][i]

        return cur
