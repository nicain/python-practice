"""Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k"""

source_url = 'https://leetcode.com/problems/remove-duplicates-from-sorted-array'

title = 'Remove Duplicates from Sorted Array'

from typing import List

def answer():
   return [0,1,2,3,4]


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        unique_tail_index = 0
        read_index = 1
        while read_index < len(nums):
            if nums[unique_tail_index] != nums[read_index]:
                unique_tail_index += 1
                nums[unique_tail_index] = nums[read_index]
            read_index += 1

        return unique_tail_index+1


def test_case1():
  args = ([0,0,1,1,1,2,2,3,3,4],)
  expected_result = answer()
  result = Solution().removeDuplicates(*args)
  assert expected_result == args[0][:result]


if __name__ == "__main__":
  test_case1()