#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        '''
        Example 1:
        nums1 = [1, 3]
        nums2 = [2]

        The median is 2.0


        Example 2:
        nums1 = [1, 2]
        nums2 = [3, 4]

        The median is (2 + 3)/2 = 2.5
        '''
        tmp = []
        while len(nums1) > 0 and len(nums2) > 0:
            if nums1[0] <= nums2[0]:
                tmp.append(nums1[0])
                del nums1[0]
            else:
                tmp.append(nums2[0])
                del nums2[0]
        if len(nums1):
            for item in nums1:
                tmp.append(item)
        else:
            for item in nums2:
                tmp.append(item)

        length = len(tmp)
        if length % 2 == 1:
            mid = length / 2
            median = tmp[mid]
            return median
        elif length % 2 == 0:
            mid = length / 2
            median = tmp[mid] + tmp[mid - 1]
            return median/2.0


if __name__ == '__main__':
    result = Solution().findMedianSortedArrays(nums1=[1, 2], nums2=[3, 4])
    print result

