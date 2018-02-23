# Source : https://leetcode.com/problems/two-sum/
# Author : Bohan Shan
# Date   : 2018-02-22

'''
Given an array of integers, return indices of the two numbers
such that they add up to a specific target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

class Solution(object):
    # returns the index of the two numbers that sum to target
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        diff = 0;
        # stores the difference between target and current index in diff
        for x, val in enumerate(nums, start = 0):
            diff = target - nums[x];
            # if a number equals the diff then it must sum to target
            for y, val1 in enumerate(nums[x+1:], start=x+1):
                if nums[y] == diff:
                    return [x, y];
        return 0;
