""" 
  Description:

  Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

  You may assume that each input would have exactly one solution, and you may not use the same element twice.

  You can return the answer in any order.

  Example 1:
  Input: nums = [2,7,11,15], target = 9
  Output: [0,1]
  Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

"""
# My solution - bad timing
class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            complement = i + 1
            sum = nums[i] + nums[complement]
            if(sum==target):
                return([i, complement])
            
# O(n), hash table, solution
class Solution:
    def twoSum(self, nums, target):
        numMap = {}
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement], i]
            numMap[nums[i]] = i

        return [] # if no solution was found