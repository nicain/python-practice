"""
Given an array of integers nums and an 
integer target, return indices of the two 
numbers such that they add up to target.

You may assume that each input would have 
exactly one solution, and you may not use 
the same element twice.

You can return the answer in any order.
"""

source_url = (
  'https://leetcode.com/problems/'
  'two-sum/'
)

title = (
  'Two Sum'
)

def answer(nums, target):
  cache = {}
  for ii, num in enumerate(nums):
    if target-num in cache:
      return cache[target-num], ii
    cache[num] = ii