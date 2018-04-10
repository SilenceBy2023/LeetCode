class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        length = len(height)
        maxarea = 0
        j = 0
        k = length - 1
        while j < k:
            if height[j] < height[k]:
                maxarea = maxarea if maxarea > (k - j) * height[j] else (k - j) * height[j]
                j += 1
            else:
                maxarea = maxarea if maxarea > (k - j) * height[k] else (k - j) * height[k]
                k -= 1
        return maxarea
