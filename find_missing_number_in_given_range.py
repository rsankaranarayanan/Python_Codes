# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

 

# Example 1:

# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]
# Example 2:

# Input: nums = [1,1]
# Output: [2]
 

# Constraints:

# n == nums.length
# 1 <= n <= 105
# 1 <= nums[i] <= n
 

# Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
#solution 1:
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums_len=len(nums)
        temp_list = list()
        for i in range(1,nums_len+1):
            if i not in nums:
                temp_list.append(i)
                
        return(temp_list)

#Solution 2:
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length_nums = len(nums)
        all_numbers_set = set(range(1, length_nums + 1))

        for num in nums:
            if num in all_numbers_set:
                all_numbers_set.remove(num)
                
        return all_numbers_set