#Median of Two Sorted Arrays

#There are two sorted arrays nums1 and nums2 of size m and n respectively.

#Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

#You may assume nums1 and nums2 cannot be both empty.

#Example 1:

#nums1 = [1, 3]
#nums2 = [2]

#The median is 2.0
#Example 2:

#nums1 = [1, 2]
#nums2 = [3, 4]

#The median is (2 + 3)/2 = 2.5

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        newlist = nums1 + nums2
        newlist.sort()
        numslen = len(nums1)
        numslen2 = len(nums2)
        total = (numslen + numslen2)
        if (total % 2) == 0:
            index = total/2
            return float((newlist[index - 1] + newlist[index]))/2
        else:
            index = total/2
            return newlist[index]
            